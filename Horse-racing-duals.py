import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
L=[]
D=10**9
for i in range(n):
    L.append(int(input()))
L.sort()
for i in range(1,n):
    if L[i]-L[i-1]<D:
        D=L[i]-L[i-1]
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(D)
