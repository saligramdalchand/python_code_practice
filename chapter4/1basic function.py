#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:42:10 2018

@author: dc
"""
#this program is tp find out the maximum out of the two

def maxVal(x,y):
    if x>y:
        return 'the biggest from the both is',x
    elif x == y:
        return "both are equal"
    else:
        return 'the biggest from the both is',y

print(maxVal(26,35))  
  
a = int(input('please provide the first value to compare: '))
b = int(input("please provide the second value to compare: "))
value = maxVal(a,b)
print (value)
