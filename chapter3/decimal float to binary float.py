#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 12:07:38 2018

@author: dc
"""

number = float(input("please provide any number between 0 and 1: "))
p = 0
remainder = 0.0
result = ''
while((2**p)*number)%1 != 0:
    remainder = (2**p)*number
    print("Remainder for the number is",remainder-int(remainder))
    p += 1
#print (p)
store_of_working_value = 0
working_value = int((2**p)*number)
store_of_working_value = working_value
if working_value == 0:
    result = '0'

while working_value > 0:
    result = str(working_value%2)+result
    working_value = working_value//2
for i in range(p-len(result)):
    result = '0'+result
    
result = result[0:-p]+'.'+result[-p:]
print(result)