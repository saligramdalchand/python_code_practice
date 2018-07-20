#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:32:10 2018

@author: dc
"""

"""
Title : finding the cube root of a given integer
"""

x= int(input("Please provide the number of which you want to get the cube root: "))
Ans= 0
while (Ans**3<abs(x)):
    Ans = Ans+1
if Ans**3 != abs(x):
    print ('the number', x ,'is not perfect cube root' )
else:
    if x < 0:
        Ans = -Ans
    print ('the cube root of the given number', x , 'is', Ans)
    