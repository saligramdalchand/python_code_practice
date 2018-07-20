#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:49:03 2018

@author: dc
"""

#this program is for finding the square of a number and also creating the test function
#this program is also helpful in  understanding docstring
 
def findroot(x, power, epsilon):
    """ this program takes x and epsilon either in float or in int form and power in int
        power >= 1 and epsilon > 0
        negative number do not have any even power value
        program returns x if x ** power is within epsilon else None
    """
    if x < 0 and power%2 == 0:
        return None
    low = min(-1, x)
    high = max (1.0, x)
    ans = (low+high)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (low+high)/2.0
    return ans

def testfindroot():
    epsilon = 0.0001
    for x in [0.25, -0.25, -2, 2, -8, 8]:
        for power in range(1,4):
            print('testing x =', str(x),'and power =', power)
            result = findroot(x, power, epsilon)
        if result == None:
            print ("    No root")
        else:
            print('result =',result,'and power =',power)
            print ("    ",result**power,'=~',x)
testfindroot()
help(findroot)