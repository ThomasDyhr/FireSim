"""
Reinforcement strength in case of fire. Calculates the sectional forces of reinforcement affected by higher temperatures due to fire
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        A: List of cross-sectional areas of each reinforcement bar in the section [mm2]
        fyk: Characteristic steel strength at 20C in [MPa] - Default: 550
        Es: Steel E-modulus at 20C in [GPa] - Default: 210
        γm: Partial factor
        ξsHot: List of Deterioration factors - HOT condition
        ξsCold: List of Deterioration factors - COLD condition
    Returns:
        Fsu: Ultimate force of each reinforcement bar in the section [kN]
        Fsd: Design force of each reinforcement bar in the section [kN]
        FsHot: Resulting force of each reinforcement bar in the section due to fire - HOT condition [kN]
        FsCold: Resulting force of each reinforcement bar in the section due to fire - COLD condition [kN]
        εs_min: Minimum strain of the steel
"""

ghenv.Component.Name = 'Steel Strength'
ghenv.Component.NickName = 'SteelStr'
ghenv.Component.Message = 'Steel Strength v.009'

# Import classes
import ghpythonlib.components as ghcomp

# Defaults
deffyk=550
defEs=210

if not fyk:
    fyk = deffyk
if not Es:
    Es = defEs

## Calculations ##

# Characteristic strength at 20C
Fsu = [a * int(fyk)/1000 for a in A]

# Characteristic strength at 20C
Fsd = [a * int(fyk)/1000/float(γm) for a in A]

#Determine if there is an odd or even number of rebars (modulus=0 means even)
mod = ghcomp.Modulus(len(A),2)

# Multiply initial strength with degredation factor
FsHot = []
FsCold = []
for i in range(0, len(Fsu)):   
     FsHot.append(round(Fsu[i]*ξsHot[i],2))
     FsCold.append(round(Fsu[i]*ξsCold[i],2))

#Minimum strain of steel
εs_min = round(fyk/(Es*1000)*100+0.2,3)