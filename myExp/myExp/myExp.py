import os
import math
import requests

#First statement
print "Hello! Guys:)"

for parent in range(3,1000000):
    iNum=0
    for child in range(2,int(math.sqrt(parent))):
        if (parent%child)==0:
            iNum+=1
    if iNum==0:
        print parent
                