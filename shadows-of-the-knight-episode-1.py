import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
minx=miny=0  
maxy=h-1
maxx=w-1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if 'U' in bomb_dir:
        maxy=y0-1
    if 'D' in bomb_dir:
        miny=y0+1
    if 'R' in bomb_dir:
        minx=x0+1
    if 'L' in bomb_dir:
        maxx=x0-1
    x0 = minx + round((maxx-minx)/2)
    y0 =miny + round((maxy-miny)/2)
    print(x0,y0)
