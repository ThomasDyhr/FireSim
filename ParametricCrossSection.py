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
        Section: Concrete cross-section geometry
        MainBars: Geometry of main reinforcement in top and bot
        ShearBars: Geometry of shear reinforcement
"""

ghenv.Component.Name = 'CrossSection Geometry'
ghenv.Component.NickName = 'SectionGeometry'
ghenv.Component.Message = 'CrossSection Geometry v.001'

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
ConSec = rs.AddRectangle( (-Width/2,0,0) , Width, Height)

#Offsets for shear rebar position
ShearOuter = rs.OffsetCurve(ConSec, [0,0,0] , Cover)
#explode = rs.ExplodeCurves(ShearOuter)
#radius = 20
#fill = rs.CurveFilletPoints(explode[0],explode[1],radius)
#fillet1 = rs.AddFilletCurve(explode[0],explode[1],radius)
#fillet2 = rs.AddFilletCurve(explode[1],explode[2],radius)
#fillet3 = rs.AddFilletCurve(explode[2],explode[3],radius)
#fillet4 = rs.AddFilletCurve(explode[3],explode[0],radius)
#fillet = [fillet1,fillet2,fillet3,fillet4]


ShearInner = rs.OffsetCurve(ConSec, [0,0,0], Cover+ShearBars[0])




Shear = [ShearOuter[0],ShearInner[0]]

#print rec
Section = ConSec
ShearBars = Shear
MainBars = fill