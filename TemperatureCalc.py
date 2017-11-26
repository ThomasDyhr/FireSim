"""
Temperature Calculation. Calculates temperatures in 1-side exposed cross-section
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Sides: Number of sides exposed ( 1 = 1-side, 2 = 2 parallel sides, 2.5 = 1 side + bottom, 3 = 2 sides + bottom, 4 = all four sides )
        t: Time step for standard fire [min]
        W: Total width of cross-section [mm]
        H: Total height of cross-section [mm]
        x: x-coordinates for temperature calculation [mm]
        y: y-coordinates for temperature calculation [mm]
        rho: Density
    Returns:
        Txy: Temperature at distance x [°C]
        TM: Temperature at middle of cross-section [°C]
        Tmm: Temperature for each millimeter of the cross-section [°C]
"""

ghenv.Component.Name = 'Temperature Calculation'
ghenv.Component.NickName = 'TempCalc'
ghenv.Component.Message = 'Temperature Calculation v.004'

#Import classes
from math import log10, exp, pi, sqrt, sin

## Code ##

cp = 1000
Lambda = 0.75
k = sqrt((pi*rho*cp)/(750*Lambda*t))

def TempCalc(t,k,xy):
    Temp = 312*log10(8*t+1)*exp(-1.9*k*(xy/1000))*sin((pi/2)-k*(xy/1000))
    return Temp

def TempCalc2(t,k,xy):
    Temp2 = ((TempCalc(t,k,xy)+TempCalc(t,k,W-xy))*(TempCalc(t,k,0)/(TempCalc(t,k,0)+TempCalc(t,k,W))))
    return Temp2

if t<1:
    Txy=20
    TM=20
else:
    Txy = []
    Tmm = []
# Calculation for 1 side exposure
    if Sides == 1:
        for i in range(len(x)):
            Txy.append(round(TempCalc(t,k,x[i]),2))
        # Temperatue at middle of cross-section
        TM = round(TempCalc(t,k,W/2),2)
        # If temperature is lower than 0 it is set to 0 !!
        if TM < 20:
            TM = 20
        # Temperatue at each mm of the cross-section
        for i in range(1,W-1):
            Temp = round(TempCalc(t,k,i),2) 
            # If temperature is lower than 0 it is set to 0 !!
            if Temp < 20:
                Temp = 20
            Tmm.append(Temp)

# Calculation for 2 parallel sides exposed
    elif Sides == 2:
        for i in range(len(x)):
            Txy.append(round( TempCalc2(t,k,x[i]) ,2))
        # Temperatue at middle of cross-section
        TM = round( TempCalc2(t,k,W/2)  ,2)
        # If temperature is lower than 0 it is set to 0 !!
        if TM < 20:
            TM = 20
        # Temperatue at each mm of the cross-section
        for i in range(1,W-1):
            Temp = round( TempCalc2(t,k,i)   ,2) 
            # If temperature is lower than 0 it is set to 0 !!
            if Temp < 20:
                Temp = 20
            Tmm.append(Temp)
