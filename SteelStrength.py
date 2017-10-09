"""
FireSim - Reinforcement strength in case of fire. Calculates the sectional forces of reinforcement affected by higher temperatures due to fire
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Area: List of cross-sectional areas of each reinforcement bar in the section in [mm2]
        Str: Steel strength at 20C in [MPa]
        Xi_T: List of Deterioration factors for half of the reinforcement bars in the section due to symmetry
    Returns:
        Fsu: Ultimate force of each reinforcement bar in the section [kN]
        Fs: Resulting force of each reinforcement bar in the section due to fire [kN]
"""

ghenv.Component.Name = 'Steel_Strength'
ghenv.Component.NickName = 'Steel Strength'
ghenv.Component.Message = 'Steel Strength v.002'

# Import classes
import ghpythonlib.components as ghcomp

## Calculations ##

# Initial strength at 20C
Fsu = [a * int(Str)/1000 for a in Area]

#Determine if there is an odd or even number of rebars (modulus=0 means even)
mod = ghcomp.Modulus(len(Area),2)

#Extend list of degredation factors to fit the number of rebars
if mod==0:
    XiT=ghcomp.InsertItems(Xi_T,list(reversed(Xi_T)),len(Xi_T))
else:
    XiT=ghcomp.InsertItems(Xi_T,Xi_T,len(Xi_T))
    XiT.pop()

# Multiply initial strength with degredation factor
Fs = []                        
for i in range(0, len(Fsu)):   
     Fs.append(round(Fsu[i]*XiT[i],2))
