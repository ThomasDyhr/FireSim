"""
Applied load calculation. Calculates the moment and shear forces in a beam based on the support conditions
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Loads: Applied load on beams [kN/m] or [kN] - Default: 40
        LoadType: Load type - (0=uniform distributed | 1=point load in middle or end(cantilever)) - Default: 0
        Support: Support conditions - (0=Simply supported both ends | 1=Cantilever) - Default: 0
        Lengths: Length of beams [m] - Default: 5
    Returns:
        Mmax: Resulting moment [kNm]
        Vmax: Resulting shear force [kN]
        LoadSet: Load settings as list
"""

ghenv.Component.Name = 'Load Calculation'
ghenv.Component.NickName = 'LoadCalc'
ghenv.Component.Message = 'Load Calculation v. 1.0'

# Import classes

## Calculations ##

# Defaults

defLoads = 40
defLoadType = 0 
defSupport = 0
defLengths = 5

if not Loads:
    Loads = defLoads
if not LoadType:
    LoadType = defLoadType
if not Support:
    Support = defSupport
if not Lengths:
    Lengths = defLengths


#Max Moment force
if Support == 0:
    if LoadType == 0:
        Mmax = 1/8*Loads*Lengths*Lengths
    elif LoadType == 1:
        Mmax = 1/4*Loads*Lengths
elif Support == 1:
    if LoadType == 0:
        Mmax = -1/2*Loads*Lengths*Lengths
    elif LoadType == 1:
        Mmax = -Loads*Lengths

#Max Shear force
if Support == 0:
    if LoadType == 0:
        Vmax = 1/2*Loads*Lengths
    elif LoadType == 1:
        Vmax = 1/2*Loads
elif Support == 1:
    if LoadType == 0:
        Vmax = Loads*Lengths
    elif LoadType == 1:
        Vmax = Loads

Mmax = round(Mmax,2)
Vmax = round(Vmax,2)
LoadSet = [Loads , LoadType , Support]