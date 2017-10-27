"""
Main Rebar Layout. Component that returns the settings for Main Rebars
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Size: Diamter of main rebars [mm]
        Number: Number of main rebars
    Returns:
        MainBars: Main rebar settings for the cross-section 
"""

ghenv.Component.Name = 'Main Reinforcement'
ghenv.Component.NickName = 'MainRebars'
ghenv.Component.Message = 'Main Reinforcement v.001'

## Code ##

#Defaults
defSize = 16
defNumber = 4

if not Size:
    Size = defSize
if not Number:
    Number = defNumber

#Output list
MainBars = []
MainBars.append(Size)
MainBars.append(Number)
