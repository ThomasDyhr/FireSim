"""
FireSim - Reinforcement strength in case of fire. Calculates the sectional forces of reinforcement affected by higher temperatures due to fire
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Area: List of cross-sectional areas of each reinforcement bar in the section in [mm2]
        fs: Steel strength at 20C in [MPa]
        Es: Steel E-modulus at 20C in [GPa]
        ξT: List of Deterioration factors for half of the reinforcement bars in the section due to symmetry
    Returns:
        Fsu: Ultimate force of each reinforcement bar in the section [kN]
        Fs: Resulting force of each reinforcement bar in the section due to fire [kN]
        εs_min: Minimum strain of the steel
"""

ghenv.Component.Name = 'Steel_Strength'
ghenv.Component.NickName = 'Steel Strength'
ghenv.Component.Message = 'Steel Strength v.003'

# Import classes
import ghpythonlib.components as ghcomp

## Calculations ##

# Initial strength at 20C
Fsu = [a * int(fs)/1000 for a in Area]

#Determine if there is an odd or even number of rebars (modulus=0 means even)
mod = ghcomp.Modulus(len(Area),2)

#Extend list of degredation factors to fit the number of rebars
if mod==0:
    XiT=ghcomp.InsertItems(ξT,list(reversed(ξT)),len(ξT))
else:
    XiT=ghcomp.InsertItems(ξT,ξT,len(ξT))
    XiT.pop()

# Multiply initial strength with degredation factor
Fs = []                        
for i in range(0, len(Fsu)):   
     Fs.append(round(Fsu[i]*XiT[i],2))


εs_min = round(fs/(Es*1000)*100+0.2,3)