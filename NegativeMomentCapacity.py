"""
Negative moment capacity in case of fire. Calculates the negative moment capacity of a cantilever beam with reinforcement in the top part of the section
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Fsu: Ultimate force of each reinforcement bar in the section [kN]
        Fsd: Design force of each reinforcement bar in the section [kN]
        FsHot: Resulting force of each reinforcement bar in the section due to fire - HOT condition [kN]
        FsCold: Resulting force of each reinforcement bar in the section due to fire - COLD condition [kN]
        εs_min: Minimum strain of the steel
        fcc: Concrete strength at 20C in [MPa] - Default: 30
        W: Width of cross-section [mm] - Default: 250
        ds: Depth of steel layer from compressed edge [mm]
        ξcMHot: Deterioration factor of concrete in mid section - HOT condition
        ξcMCold: Deterioration factor of concrete in mid section - COLD condition
        ηHot: Stress Distribution Factor - HOT condition
        ηCold: Stress Distribution Factor - COLD condition
    Returns:
        Md: Positive moment capacity - Design Value [kNm]
        Mstart: Positive moment capacity - Start of Fire [kNm]
        Mhot: Positive moment capacity - HOT condition [kNm]
        Mcold: Positive moment capacity - COLD condition [kNm]
        Info: Check if cross-section is over-reinforced
"""

ghenv.Component.Name = 'Negative Moment Capacity'
ghenv.Component.NickName = 'NegMomentCapacity'
ghenv.Component.Message = 'Negative Moment Capacity v. 1.0'

# Import classes

# Defaults
deffcc=30
defW=250
defξcMHot=1
defξcMCold=1
defηHot=1
defηCold=1
defy=1
defds=1

if not fcc:
    fcc = deffcc
if not W:
    W = defW
if not ξcMHot:
    ξcMHot = defξcMHot
if not ξcMCold:
    ξcMCold = defξcMCold
if not ηHot:
    ηHot = defηHot
if not ηCold:
    ηCold = defηCold
if not ds:
    ds = defds

## Calculations ##

FsdTOT = sum(Fsd)
FsuTOT = sum(Fsu)
FsHTOT = sum(FsHot)
FsCTOT = sum(FsCold)

def MomentCalc(FsTOT,W,n,XicM,fcc,ds):
    y = round(FsTOT/(W*n*XicM*int(fcc))*1000,2) #Depth of compression zone
    Moment = round(FsTOT*(ds-(W/2)*(1-n)-y/2)/1000,2) #Moment
    return Moment,y

#Design values
Md,yd = MomentCalc(FsdTOT,W,1,1,fcc,ds)

#Start of fire
Mstart,ystart = MomentCalc(FsuTOT,W,1,1,fcc,ds)

#During Fire
Mhot,yhot = MomentCalc(FsHTOT,W,ηHot,ξcMHot,fcc,ds)

#After Fire
Mcold,ycold = MomentCalc(FsCTOT,W,ηCold,ξcMCold,fcc,ds)

#Check for over-reinforced section
def StrainCheck(ds,W,n,y,XicM):
    if not y:
        y = defy
    strain = round((ds-(W/2)*(1-n)-(5/4)*y)/((5/4)*y)*(0.35/XicM),3)
    return strain

εsDES = StrainCheck(ds,W,1,yd,1)
εsULT = StrainCheck(ds,W,1,ystart,1)
εsHOT = StrainCheck(ds,W,ηHot,yhot,ξcMHot)
εsCOLD = StrainCheck(ds,W,ηCold,ycold,ξcMHot)

if εsDES > εs_min and εsULT > εs_min and εsHOT > εs_min and εsCOLD > εs_min :
    Info = "Cross-section is NOT over-reinforced in either of the: Design, Ultimate, HOT or COLD conditions"
elif εsDES < εs_min or εsULT < εs_min or εsHOT < εs_min or εsCOLD < εs_min :
    Info = "NB! Cross-section IS over-reinforced !!"
