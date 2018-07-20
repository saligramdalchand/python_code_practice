#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:45:34 2018

@author: dc
"""
#this program is for the finding the LCM of two numbers
number1 =int(input('please provide the first number for which you want to get LCM\n' ))

number2 =int(input('please provide the second number for which you want to get LCM\n' ))

x =1

while True:
    if x%number1 ==0 and x%number2 == 0:
        print('the LCM of the number',number1,'and number',number2,'is',x)
        break
    else:
        x = x+1