"""
Main Rebar Layout. Component that returns the settings for Main Rebars
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Size: Diamter of main rebars [mm]
        Number: Number of main rebars
        Spacing: Spacing of main rebars
    Returns:
        MainBars: Main rebar settings for the cross-section 
"""

ghenv.Component.Name = 'Main Reinforcement'
ghenv.Component.NickName = 'MainRebars'
ghenv.Component.Message = 'Main Reinforcement v.001'

# Import classes

## Code ##

Size = 16
Number = 4
Spacing = 150

#if Size:
#    print 'test'

MainBars = []
MainBars.append(Size)
MainBars.append(Number)
MainBars.append(Spacing)

print MainBars