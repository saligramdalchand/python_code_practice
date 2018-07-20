#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 12:06:29 2018

@author: dc
"""

'''this program is for the getting of the cube root by using bisection method'''

number = float(input('please provide the number for which you want to get the square root\n'))
high = max(1.0,number)
low = 0
ans = (high+low)/2
iteration = 0
epsilon = 0.01

while abs(ans**2-number) >= epsilon:
    #print('the lowest value is',low,'highest value is',high,'and answer is',ans)
    iteration += 1
    if (ans**2>number):
        high = ans
    else:
        low = ans
    ans = (high+low)/2
    
print('the loop runed for the',iteration,'times')
print('the square root of the number',number,'is supposed to be near',ans)