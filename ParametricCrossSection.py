"""
Cross-section geometry. Returns the geometry of the cross-section based on input values
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Width: Widht of cross-section [mm]
        Height: Height of cross-section [mm]
        RebarsTop: Input settings for rebars in "top" of cross-section
        RebarsBot: Input settings for rebars in "bot" of cross-section
        ShearBars: Input settings for shear rebars in cross-section
        Cover: Cover thickness [mm] (From concrete edge to shear rebar's outer edge) 
    Returns:
        Section: Cross-section geometry
        AreaTop: Area of each rebar in the top layer [mm2]
        xyTop: Local xy-coordinates of half of the rebars in top of the cross-section (Due to symmetry)
        AreaBot: Area of each rebar in the bottom layer [mm2]
        xyBot: Local xy-coordinates of half of the rebars in top of the cross-section (Due to symmetry)
        ds: Distance from top/bottom edges to center of rebars [mm] (0 is for bottom bars - 1 is for top bars)
"""

ghenv.Component.Name = 'CrossSection Geometry'
ghenv.Component.NickName = 'SectionGeometry'
ghenv.Component.Message = 'CrossSection Geometry v.004'

#Import classes
import rhinoscriptsyntax as rs

## Code ##

#Defaults
#defSize = 16
#defNumber = 4

#if not Size:
#    Size = defSize
#if not Number:
#    Number = defNumber

#Create concrete section
ConSec = rs.AddRectangle( (0,0,0) , Width, Height)
explodeSec = rs.ExplodeCurves(ConSec)
TopEdgeMid = rs.CurveMidPoint(explodeSec[2])
BotEdgeMid = rs.CurveMidPoint(explodeSec[0])

#Offsets for shear rebar position
ShearOuter = rs.OffsetCurve(ConSec, TopEdgeMid , Cover)

#explode = rs.ExplodeCurves(ShearOuter)
#radius = 20
#fill = rs.CurveFilletPoints(explode[0],explode[1],radius)
#fillet1 = rs.AddFilletCurve(explode[0],explode[1],radius)
#fillet2 = rs.AddFilletCurve(explode[1],explode[2],radius)
#fillet3 = rs.AddFilletCurve(explode[2],explode[3],radius)
#fillet4 = rs.AddFilletCurve(explode[3],explode[0],radius)
#fillet = [fillet1,fillet2,fillet3,fillet4]

ShearInner = rs.OffsetCurve(ConSec, TopEdgeMid, Cover+ShearBars[0])

explodeInner = rs.ExplodeCurves(ShearInner)

#Creating Top bars
TopLine = rs.OffsetCurve(explodeInner[2], BotEdgeMid, RebarsTop[0]/2)
TopLine = rs.ExtendCurveLength(TopLine, 0, 2, -RebarsTop[0]/2)
DivTop = rs.DivideCurve(TopLine,RebarsTop[1]-1)
TopBars = []
for i in range(len(DivTop)):
    TopBars.append(rs.AddCircle(DivTop[i],RebarsTop[0]/2))
TopLineMid = rs.CurveMidPoint(TopLine)
#ds to Top bars
dsTop = rs.Distance(TopLineMid,BotEdgeMid)

#Creating Bot bars
BotLine = rs.OffsetCurve(explodeInner[0], TopLineMid, RebarsBot[0]/2)
BotLine = rs.ExtendCurveLength(BotLine, 0, 2, -RebarsBot[0]/2)
DivBot = rs.DivideCurve(BotLine,RebarsBot[1]-1)
BotBars = []
for i in range(len(DivBot)):
    BotBars.append(rs.AddCircle(DivBot[i],RebarsBot[0]/2))
BotLineMid = rs.CurveMidPoint(BotLine)
#ds to bot bars
dsBot = rs.Distance(BotLineMid,TopEdgeMid)

#Output
Section = [ConSec]
for i in range(len(TopBars)):
    Section.append(TopBars[i])
for i in range(len(BotBars)):
    Section.append(BotBars[i])
Section.append(ShearOuter[0])
Section.append(ShearInner[0])

AreaTop = []
for i in TopBars:
    AreaTop.append(int(rs.Area(i)))

xyTop = []
DivTop.reverse()
for i in range(int(round(len(DivTop)/2))):
    xyTop.append(DivTop[i])

AreaBot = []
for i in BotBars:
    AreaBot.append(int(rs.Area(i)))

xyBot = []
for i in range(int(round(len(DivBot)/2))):
    xyBot.append(DivBot[i])

ds = [dsBot,dsTop]
