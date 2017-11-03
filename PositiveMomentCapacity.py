"""
Positive moment capacity in case of fire. Calculates the positive moment capacity of a beam with reinforcement in the bottom part of the section
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Fsu: Ultimate force of each reinforcement bar in the section [kN]
        Fsd: Design force of each reinforcement bar in the section [kN]
        FsHOT: Resulting force of each reinforcement bar in the section due to fire - HOT condition [kN]
        FsCOLD: Resulting force of each reinforcement bar in the section due to fire - COLD condition [kN]
        εs_min: Minimum strain of the steel
        fcc: Concrete strength at 20C in [MPa]
        W: Width of cross-section [mm]
        ds: Depth of steel layer from compressed edge [mm]
        XicMHot: Deterioration factor of concrete in mid section - HOT condition
        XicMCold: Deterioration factor of concrete in mid section - COLD condition
        nHot: Stress Distribution Factor - HOT condition
        nCold: Stress Distribution Factor - COLD condition
    Returns:
        Md: Positive moment capacity - Design Value [kNm]
        Mstart: Positive moment capacity - Start of Fire [kNm]
        Mhot: Positive moment capacity - HOT condition [kNm]
        Mcold: Positive moment capacity - COLD condition [kNm]
        Info: Check if cross-section is over-reinforced
"""

ghenv.Component.Name = 'Positive_Moment_Capacity'
ghenv.Component.NickName = 'PosMomentCapacity'
ghenv.Component.Message = 'Positive Moment Capacity v.005'

# Import classes

## Calculations ##

FsdTOT = sum(Fsd)
FsuTOT = sum(Fsu)
FsHTOT = sum(FsHOT)
FsCTOT = sum(FsCOLD)
ds = ds[0]

def MomentCalc(FsTOT,W,n,Xic,fcc,ds):
    y = round(FsTOT/(W*n*Xic*int(fcc))*1000,2) #Depth of compression zone
    Moment = round(FsTOT*(ds-y/2)/1000,2) #Moment
    return Moment,y

#Design values
Md,yd = MomentCalc(FsdTOT,W,1,1,fcc,ds)

#Start of fire
Mstart,ystart = MomentCalc(FsuTOT,W,1,1,fcc,ds)

#During Fire
Mhot,yhot = MomentCalc(FsHTOT,W,nHot,XicMHot,fcc,ds)

#After Fire
Mcold,ycold = MomentCalc(FsCTOT,W,nCold,XicMCold,fcc,ds)

#Check for over-reinforced section
εsDES = round((ds-(5/4)*yd)/((5/4)*yd)*(0.35),3)
εsULT = round((ds-(5/4)*ystart)/((5/4)*ystart)*(0.35),3)
εsHOT = round((ds-(5/4)*yhot)/((5/4)*yhot)*(0.35/XicMHot),3)
εsCOLD = round((ds-(5/4)*ycold)/((5/4)*ycold)*(0.35/XicMCold),3)

if εsDES > εs_min and εsULT > εs_min and εsHOT > εs_min and εsCOLD > εs_min :
    Info = "Cross-section is NOT over-reinforced in either of the: Design, Ultimate, HOT or COLD conditions"
elif εsDES < εs_min or εsULT < εs_min or εsHOT < εs_min or εsCOLD < εs_min :
    Info = "NB! Cross-section IS over-reinforced !!"
