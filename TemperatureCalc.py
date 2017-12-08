"""
Temperature Calculation. Calculates temperatures in 1-side to 4-side exposed cross-sections
-----
FireSim made by Thomas Dyhr, DTU.BYG

    Args:
        Sides: Number of sides exposed ( 0 = Bottom side, 1 = 1 side, 2 = 2 parallel sides, 2.5 = 1 side + bottom, 3 = 2 sides + bottom, 4 = all four sides )
        t: Time step for standard fire [min]
        W: Total width of cross-section [mm]
        H: Total height of cross-section [mm]
        x: x-coordinates for temperature calculation [mm]
        y: y-coordinates for temperature calculation [mm]
        rho: Density
        n: Number of lamellas to evaluate for
    Returns:
        Txy: Temperature at distance x [°C]
        TM: Temperature at middle of cross-section [°C]
        Tmm: Temperature for each millimeter of the cross-section [°C]
"""

ghenv.Component.Name = 'Temperature Calculation'
ghenv.Component.NickName = 'TempCalc'
ghenv.Component.Message = 'Temperature Calculation v.008'

#Import classes
from math import log10, exp, pi, sqrt, sin

## Code ##

cp = 1000
Lambda = 0.75

def TempCalc(t,k,x):
    Temp = 312*log10(8*t+1)*exp(-1.9*k*(x/1000))*sin((pi/2)-k*(x/1000))
    return Temp

def TempCalc2X(t,k,x):
    Temp2X = ((TempCalc(t,k,x)+TempCalc(t,k,W-x))*(TempCalc(t,k,0)/(TempCalc(t,k,0)+TempCalc(t,k,W))))
    return Temp2X

def TempCalc2Y(t,k,y):
    Temp2Y = ((TempCalc(t,k,y)+TempCalc(t,k,H-y))*(TempCalc(t,k,0)/(TempCalc(t,k,0)+TempCalc(t,k,H))))
    return Temp2Y

def TempCalc25(t,k,x,y):
    Temp25 = TempCalc(t,k,x)+TempCalc(t,k,y)-((TempCalc(t,k,x)*TempCalc(t,k,y))/TempCalc(t,k,0))
    return Temp25

def TempCalc3(t,k,x,y):
    Temp3 = TempCalc2X(t,k,x)+TempCalc(t,k,y)-((TempCalc2X(t,k,x)*TempCalc(t,k,y))/TempCalc(t,k,0))
    return Temp3

def TempCalc4(t,k,x,y):
    Temp4 = TempCalc2X(t,k,x)+TempCalc2Y(t,k,y)-((TempCalc2X(t,k,x)*TempCalc2Y(t,k,y))/TempCalc(t,k,0))
    return Temp4


if t<1:
    Txy = [20 for i in y]
    TM=20
    Tmm = [20 for i in range(0,n)]
else:
    Txy = []
    Tmm = []
    k = sqrt((pi*rho*cp)/(750*Lambda*t))

# Calculation for Bottom exposure
    if Sides == 0:
        for i in range(len(y)):
            Txy.append(round(TempCalc(t,k,y[i]),2))
        # Temperatue at middle of cross-section
        TM = round(TempCalc(t,k,H/2),2)
        # Temperatue in middle of each lamella
        for i in range(1,n*2,2):
            Y = H/n/2*i
            Temp = round(TempCalc(t,k,Y),2) 
            Tmm.append(Temp)

# Calculation for 1 side exposure
    if Sides == 1:
        for i in range(len(x)):
            Txy.append(round(TempCalc(t,k,x[i]),2))
        # Temperatue at middle of cross-section
        TM = round(TempCalc(t,k,W/2),2)
        # Temperatue in middle of each lamella
        for i in range(1,n*2,2):
            X = W/n/2*i
            Temp = round(TempCalc(t,k,X),2) 
            Tmm.append(Temp)

# Calculation for 2 parallel sides exposed
    elif Sides == 2:
        for i in range(len(x)):
            Txy.append(round( TempCalc2X(t,k,x[i]) ,2))
        # Temperatue at middle of cross-section
        TM = round( TempCalc2X(t,k,W/2) ,2)
        # Temperatue in middle of each lamella
        for i in range(1,n*2,2):
            X = W/n/2*i
            Temp = round( TempCalc2X(t,k,X) ,2) 
            Tmm.append(Temp)

# Calculation for 1 side + bottom exposed
    elif Sides == 2.5:
        for i in range(len(x)):
            Txy.append(round( TempCalc25(t,k,x[i],y[i]) ,2))
        # Temperatue at middle of cross-section
        TM = round( TempCalc25(t,k,W/2,H/2)  ,2)
        # Temperatue in middle of each lamella
        for i in range(1,n*2,2):
            X = W/n/2*i
            for j in range(1,n*2,2):
                Y = H/n/2*j
                Temp = round( TempCalc25(t,k,X,Y) ,2)
                Tmm.append(Temp)

# Calculation for 3 sides exposed
    elif Sides == 3:
        for i in range(len(x)):
            Txy.append(round( TempCalc3(t,k,x[i],y[i]) ,2))
        # Temperatue at middle of cross-section
        TM = round( TempCalc3(t,k,W/2,H/2)  ,2)
        # Temperatue in middle of each lamella
        for i in range(1,n*2,2):
            X = W/n/2*i
            for j in range(1,n*2,2):
                Y = H/n/2*j
                Temp = round( TempCalc3(t,k,X,Y) ,2)
                Tmm.append(Temp)

# Calculation for 4 sides exposed
    elif Sides == 4:
        for i in range(len(x)):
            Txy.append(round( TempCalc4(t,k,x[i],y[i]) ,2))
        # Temperatue at middle of cross-section
        TM = round( TempCalc4(t,k,W/2,H/2)  ,2)
        # Temperatue in middle of each lamella
        for i in range(1,n*2,2):
            X = W/n/2*i
            for j in range(1,n*2,2):
                Y = H/n/2*j
                Temp = round( TempCalc4(t,k,X,Y) ,2)
                Tmm.append(Temp)

# Replacing all temperatures below 20°C with 20°C
Txy[:] = [20 if i<20 else i for i in Txy]
if TM < 20:
    TM = 20
Tmm[:] = [20 if i<20 else i for i in Tmm]