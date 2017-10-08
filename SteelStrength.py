"""
FireSim - Reinforcement strength in case of fire. Calculates the sectional force of reinforcement affected by higher temperatures due to fire
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Area: List of cross-sectional areas of each reinforcement bar in the section
        YieldStr: Steel strength at 20C
        Xi(T): List of Degredation factors for each reinforcement bar in the section
    Returns:
        Fsu: Resulting strength of each reinforcement bar
"""

# Add the message thingie underneath the component
ghenv.Component.Name = 'Steel_Strength'
ghenv.Component.NickName = 'Steel Strength'
ghenv.Component.Message = 'Steel Strength v.0.1'

# Importing classes and modules
import Rhino as rc

# Setting defaults

list1 = Area
list2 = [a * int(YieldStr)/1000 for a in list1]

Fsu = list2

