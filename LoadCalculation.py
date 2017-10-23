"""
Applied load calculation. Calculates the moment and shear capacity of a beam based on the support conditions
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Loads: Applied load on beams [kN/m] or [kN]
        LoadType: Load type - (0=uniform distributed | 1=point load in middle or end(cantilever))
        Support: Support conditions - (0=Simply supported both ends | 1=Cantilever)
        Lengths: Length of beams [m]
    Returns:
        M: Resulting moment [kNm]
        V: Resulting shear force [kN]
"""

ghenv.Component.Name = 'Load_Calculation'
ghenv.Component.NickName = 'LoadCalc'
ghenv.Component.Message = 'Load Calculation v.001'

# Import classes

## Calculations ##

if Support == 0:
    if LoadType == 0:
        M = 1/8*Loads*Lengths*Lengths
    elif LoadType == 1:
        M = 1/4*Loads*Lengths
elif Support == 1:
    if LoadType == 0:
        M = -1/2*Loads*Lengths*Lengths
    elif LoadType == 1:
        M = -Loads*Lengths

M = round(M,2)
#V = round(V,2)