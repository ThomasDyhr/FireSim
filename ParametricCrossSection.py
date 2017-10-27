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
#explode = rs.ExplodeCurves(Off1)

ShearInner = rs.OffsetCurve(ConSec, [0,0,0], Cover+ShearBars[0])

Shear = [ShearOuter[0],ShearInner[0]]

#print rec
Section = ConSec
ShearBars = Shear
