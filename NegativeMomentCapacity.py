"""
Negative moment capacity in case of fire. Calculates the negative moment capacity of a cantilever beam with reinforcement in the top part of the section
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

ghenv.Component.Name = 'Negative_Moment_Capacity'
ghenv.Component.NickName = 'NegMomentCapacity'
ghenv.Component.Message = 'Negative Moment Capacity v.001'

# Import classes

## Calculations ##

FsdTOT = sum(Fsd)
FsuTOT = sum(Fsu)
FsHTOT = sum(FsHOT)
FsCTOT = sum(FsCOLD)
ds = ds[1]

def MomentCalc(FsTOT,W,n,XicM,fcc,ds):
    y = round(FsTOT/(W*n*XicM*int(fcc))*1000,2) #Depth of compression zone
    Moment = round(FsTOT*(ds-(W/2)*(1-n)-y/2)/1000,2) #Moment
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
def StrainCheck(ds,W,n,y,XicM):
    strain = round((ds-(W/2)*(1-n)-(5/4)*y)/((5/4)*y)*(0.35/XicM),3)
    return strain

εsDES = StrainCheck(ds,W,1,yd,1)
εsULT = StrainCheck(ds,W,1,ystart,1)
εsHOT = StrainCheck(ds,W,nHot,yhot,XicMHot)
εsCOLD = StrainCheck(ds,W,nCold,ycold,XicMHot)

if εsDES > εs_min and εsULT > εs_min and εsHOT > εs_min and εsCOLD > εs_min :
    Info = "Cross-section is NOT over-reinforced in either of the: Design, Ultimate, HOT or COLD conditions"
elif εsDES < εs_min or εsULT < εs_min or εsHOT < εs_min or εsCOLD < εs_min :
    Info = "NB! Cross-section IS over-reinforced !!"
