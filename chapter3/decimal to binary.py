#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:36:49 2018

@author: dc
"""

# to convert decimal into binary

number = int(input('please provide the number that is going to be your target '))
isNeg = False
result = ''
if number < 0:
    isNeg = True
    number = abs(number)
if number == 0:
    result = '0'
while (number>0):
    result = str(number%2)+result
    number = number//2
if isNeg:
    result = '-'+result
print(result)