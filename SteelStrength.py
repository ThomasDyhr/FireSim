"""
Reinforcement strength in case of fire. Calculates the sectional forces of reinforcement affected by higher temperatures due to fire
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        A: List of cross-sectional areas of each reinforcement bar in the section in [mm2]
        fyk: Characteristic steel strength at 20C in [MPa]
        Es: Steel E-modulus at 20C in [GPa]
        γm: Partial factor
        ξsHOT: List of Deterioration factors for half of the reinforcement bars in the section due to symmetry - HOT condition
        ξsCOLD: List of Deterioration factors for half of the reinforcement bars in the section due to symmetry - COLD condition
    Returns:
        Fsu: Ultimate force of each reinforcement bar in the section [kN]
        Fsd: Design force of each reinforcement bar in the section [kN]
        FsHOT: Resulting force of each reinforcement bar in the section due to fire - HOT condition [kN]
        FsCOLD: Resulting force of each reinforcement bar in the section due to fire - COLD condition [kN]
        εs_min: Minimum strain of the steel
"""

ghenv.Component.Name = 'Steel_Strength'
ghenv.Component.NickName = 'Steel Strength'
ghenv.Component.Message = 'Steel Strength v.007'

# Import classes
import ghpythonlib.components as ghcomp

## Calculations ##

# Characteristic strength at 20C
Fsu = [a * int(fyk)/1000 for a in A]

# Characteristic strength at 20C
Fsd = [a * int(fyk)/1000/float(γm) for a in A]

#Determine if there is an odd or even number of rebars (modulus=0 means even)
mod = ghcomp.Modulus(len(A),2)

#Extend list of degredation factors to fit the number of rebars
if mod==0:
    XiHOT=ghcomp.InsertItems(ξsHOT,list(reversed(ξsHOT)),len(ξsHOT))
    XiCOLD=ghcomp.InsertItems(ξsCOLD,list(reversed(ξsCOLD)),len(ξsCOLD))
else:
    XiHOT=ghcomp.InsertItems(ξsHOT,ξsHOT,len(ξsHOT))
    XiHOT.pop()
    XiCOLD=ghcomp.InsertItems(ξsCOLD,ξsCOLD,len(ξsCOLD))
    XiCOLD.pop()

# Multiply initial strength with degredation factor
FsHOT = []
FsCOLD = []
for i in range(0, len(Fsu)):   
     FsHOT.append(round(Fsu[i]*XiHOT[i],2))
     FsCOLD.append(round(Fsu[i]*XiCOLD[i],2))

#Minimum strain of steel
εs_min = round(fyk/(Es*1000)*100+0.2,3)