"""
Stirrup Layout. Component that returns the settings for stirrups
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Size: Diameter of stirrups [mm] - Default: 12
        Spacing: Spacing of stirrups - Default: 150
    Returns:
        Stirrups: Stirrup settings for the cross-section 
"""

ghenv.Component.Name = 'Stirrup Reinforcement'
ghenv.Component.NickName = 'Stirrups'
ghenv.Component.Message = 'Stirrup Reinforcement v. 1.0'

## Code ##

#Defaults
defSize = 12
defSpacing = 150

if not Size:
    Size = defSize
if not Spacing:
    Spacing = defSpacing

#Output list
Stirrups = []
Stirrups.append(Size)
Stirrups.append(Spacing)