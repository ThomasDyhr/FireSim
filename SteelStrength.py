"""
FireSim - Reinforcement strength in case of fire. Calculates the sectional force of reinforcement affected by higher temperatures due to fire
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Area: List of cross-sectional areas of each reinforcement bar in the section in [mm2]
        Str: Steel strength at 20C in [MPa]
        Xi_T: List of Degredation factors for each reinforcement bar in the section
    Returns:
        Fsu: Resulting strength of each reinforcement bar [kN]
"""

# Add the message thingie underneath the component
ghenv.Component.Name = 'Steel_Strength'
ghenv.Component.NickName = 'Steel Strength'
ghenv.Component.Message = 'Steel Strength v.0.1'

# Import classes
import ghpythonlib.components as ghcomp

## Calculations ##

# Initial strength at 20C
Fsu0 = [a * int(Str)/1000 for a in Area]

#Determine if there is an odd or even number of rebars (modulus=0 means even)
mod = ghcomp.Modulus(len(Area),2)

#Extend list of degredation factors to fit the number of rebars
if mod==0:
    XiT=ghcomp.InsertItems(Xi_T,Xi_T,len(Xi_T))
else:
    XiT=ghcomp.InsertItems(Xi_T,Xi_T,len(Xi_T))
    XiT.pop()


Fsu = []                        #Create empty list
for i in range(0, len(Fsu0)):
     Fsu.append(round(Fsu0[i]*XiT[i],2))

