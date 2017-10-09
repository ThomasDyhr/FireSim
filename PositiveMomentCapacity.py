"""
Positive moment capacity in case of fire. Calculates the positive moment capacity of a beam with reinforcement in the bottom part of the section
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Fsu: Ultimate force of each reinforcement bar in the section [kN]
        Fs: Resulting force of each reinforcement bar in the section due to fire [kN]
        εs_min: Minimum strain of the steel
        fcc: Concrete strength at 20C in [MPa]
        W: Width of cross-section [mm]
        ds: Depth of steel layer from compressed edge [mm]
        XicMHot: Deterioration factor of concrete in mid section - HOT condition
        XicMCold: Deterioration factor of concrete in mid section - COLD condition
        nHot: Stress Distribution Factor - HOT condition
        nCold: Stress Distribution Factor - COLD condition
    Returns:
        Mstart: Positive moment capacity - Before Fire [kNm]
        Mhot: Positive moment capacity - HOT condition [kNm]
        Mcold: Positive moment capacity - COLD condition [kNm]
        Info: Check if cross-section is over-reinforced
"""

ghenv.Component.Name = 'Moment_Capacity'
ghenv.Component.NickName = 'Moment Capacity'
ghenv.Component.Message = 'Moment Capacity v.001'

# Import classes
import ghpythonlib.components as ghcomp

## Calculations ##

FsuTOT = sum(Fsu)
FsTOT = sum(Fs)

#Before Fire
y0 = round(FsuTOT/(W*fcc)*1000,2) #Depth of compression zone
Mstart = round(FsuTOT*(ds-y0/2)/1000,2) #Moment

#During Fire
y1 = round(FsTOT/(W*nHot*XicMHot*fcc)*1000,2) #Depth of compression zone
Mhot = round(FsTOT*(ds-y1/2)/1000,2) #Moment

#After Fire
y2 = round(FsuTOT/(W*nCold*XicMCold*fcc)*1000,2) #Depth of compression zone
Mcold = round(FsuTOT*(ds-y2/2)/1000,2) #Moment


#Check for over-reinforced section
εs = round((ds-(5/4)*y2)/((5/4)*y2)*(0.35/XicMCold),3)
if εs > εs_min:
    Info = "Cross-section is NOT over-reinforced"
else:
    Info = "Cross-section IS over-reinforced"

