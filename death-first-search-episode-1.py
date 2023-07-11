import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
links=[]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links.append((n1,n2))
gate=[]
for i in range(e):
    ei = int(input())
    gate.append(ei)  # the index of a gateway node
def cut():
    for link in links:
        if link[0]==si or link[1]==si:
            if link[0] in gate or link[1] in gate:
                return link
    p=links[0]
    links.remove(links[0])
    return p

# game loop
while True:
    si = int(input())
    ct=cut()  # The index of the node on which the Bobnet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(ct[0],ct[1])
