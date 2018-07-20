#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:28:21 2018

@author: dc
"""

#cube root with the use of the for loop

number = int(input('please provide the number for cube root \n'))
#there is no need for assigning the new variable as it comes along with for loop

for ans in range(0, abs(number)+1):
    if ans**3>=number:
        break
if ans**3 != abs(number):
    print('there is not any solution for the given number',number,'\n')
else:
    if number<0:
        ans = -ans
    print('cube root for the number',number,'is ans',ans)