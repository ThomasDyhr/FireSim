"""
Temperature Calculation. Calculates temperatures in 1-side exposed cross-section
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        t: Time step for standard fire [min]
        W: Total width of cross-section [mm]
        x: Distance for temperature calculation [mm]
        rho: Density
    Returns:
        T: Temperature at distance x [°C]
        TM: Temperature at middle of cross-section [°C]
        Tmm: Temperature for each millimeter of the cross-section [°C]
"""

ghenv.Component.Name = 'Temperature Calculation'
ghenv.Component.NickName = 'TempCalc'
ghenv.Component.Message = 'Temperature Calculation v.003'

#Import classes
from math import log10, exp, pi, sqrt, sin

## Code ##

cp = 1000
Lambda = 0.75
k = sqrt((pi*rho*cp)/(750*Lambda*t))

def TempCalc(t,k,depth):
    Temp = 312*log10(8*t+1)*exp(-1.9*k*(depth/1000))*sin((pi/2)-k*(depth/1000))
    return Temp

#Temp1 = TempCalc(t,k,x)


if t<1:
    T=20
    TM=20
else:
    Temp1 = []
    for i in range(len(x)):
        Temp1.append(round(TempCalc(t,k,x[i]),2))
        T=Temp1
        
    # Temperatue at middle of cross-section
    TM = round(TempCalc(t,k,W/2),2)
    # If temperature is lower than 0 it is set to 0 !!
    if TM < 20:
        TM = 20
        
    # Temperatue at each mm of the cross-section
    Tmm = []
    for i in range(1,W-1):
        Temp = round(TempCalc(t,k,i),2) 
        # If temperature is lower than 0 it is set to 0 !!
        if Temp < 20:
            Temp = 20
        Tmm.append(Temp)
