import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def d(laa,lab,loa,lob):
    x=(lob-loa)*math.cos((laa+lab)/2)
    y=(lab-laa)
    return math.sqrt(x**2+y**2)*6371
lon = input()
lat = input()
lon=float(lon.replace(',','.'))
lat=float(lat.replace(',','.'))
n = int(input())
D=10**10
for i in range(n):
    defib = input()
    L=[]
    for j in defib.split(';'):
        L.append(j)
    L[5]=L[5].replace(',','.')
    L[4]=L[4].replace(',','.')
    if d(lat,float(L[5]),lon,float(L[4]))<D:
        D=d(lat,float(L[5]),lon,float(L[4]))
        p=L[1]
print(p)
