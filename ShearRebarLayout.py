"""
Shear Rebar Layout. Component that returns the settings for Shear Rebars
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Size: Diamter of rebars [mm]
        Spacing: Spacing of shear rebars
    Returns:
        ShearBars: Shear rebar settings for the cross-section 
"""

ghenv.Component.Name = 'Shear Reinforcement'
ghenv.Component.NickName = 'ShearRebars'
ghenv.Component.Message = 'Shear Reinforcement v.001'

## Code ##

#Defaults
defSize = 12
defSpacing = 150

if not Size:
    Size = defSize
if not Spacing:
    Spacing = defSpacing

#Output list
MainBars = []
MainBars.append(Size)
MainBars.append(Spacing)