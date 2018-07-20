#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:10:31 2018

@author: dc
"""

''' this program is for the finding of the very close square root to the given number'''

number = float(input('please provide the number you want to check for the square root\n'))

epsilon = 0.1
step = epsilon**2
ans = 0.0
total_iteration = 0

while (abs(ans**2-number)>= epsilon and ans<=number):
    total_iteration += 1
    ans +=step
print ('total number of the time the repeatation occur',total_iteration)
if(ans**2 - number) >= epsilon:
    print ('i am not able to find the square root of the number',number)
else:
    print ('the approx square root for the given number',number,'is the',ans)
