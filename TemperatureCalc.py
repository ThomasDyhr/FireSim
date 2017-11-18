"""
Temperature Calculation. Calculates temperatures in 1-side exposed cross-section
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        t: Time step for standard fire [min]
        W: Total width of cross-section [mm]
        x: Distance for temperature calculation [mm]
    Returns:
        T: Temperature at distance x [°C]
        TM: Temperature at middle of cross-section [°C]
        Tmm: Temperature for each millimeter of the cross-section [°C]
"""

ghenv.Component.Name = 'Temperature Calculation'
ghenv.Component.NickName = 'TempCalc'
ghenv.Component.Message = 'Temperature Calculation v.002'

#Import classes
from math import log10, exp, pi, sqrt, sin

## Code ##

#Defaults

#if not Size:
#    Size = defSize
#if not Number:
#    Number = defNumber
rho = 2300
cp = 1000
Lambda = 0.75

if t<1:
    T=20
    TM=0
else:
    k = sqrt((pi*rho*cp)/(750*Lambda*t))
    T = []
    for i in range(len(x)):
        T.append(round(312*log10(8*t+1)*exp(-1.9*k*(x[i]/1000))*sin((pi/2)-k*(x[i]/1000)),2))
        
    # Temperatue at middle of cross-section
    TM = round(312*log10(8*t+1)*exp(-1.9*k*((W/2)/1000))*sin((pi/2)-k*((W/2)/1000)),2)
    
    
    # If temperature is lower than 0 it is set to 0 !!
    if TM < 0:
        TM = 0
        
    # Temperatue at each mm of the cross-section
    Tmm = []
    for i in range(1,W-1):
        Temp=(round(312*log10(8*t+1)*exp(-1.9*k*(i/1000))*sin((pi/2)-k*(i/1000)),2))
        # If temperature is lower than 0 it is set to 0 !!
        if Temp < 0:
            Temp = 0
        Tmm.append(Temp)

print TM