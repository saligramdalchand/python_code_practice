#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 14:20:03 2018

@author: dc
"""

'''
finding the square root of the value using the newton rapson method
'''

number =  float(input('please provide the number to get the square root\n'))

guess = number/2.0
steps = 0
epsilon = 0.01
ans =  0.0
while abs(guess*guess - number) >= epsilon:
    steps += 1
    guess = guess - (((guess**2) - number)/(2*guess))
    
print (steps, guess)