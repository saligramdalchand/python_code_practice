#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:03:41 2018

@author: dc
"""

'''this program is for finding the cube root of integer either negative or positive'''
'''this program is telling me things that i done wrong in the program of getting square root of the
negative integer.. very useful but pretty basic program for someone who is a good coder '''
number = float(input("please provide the number you want to get the cube root\n"))
 
low = min(0,number)
high = max(0,number)
steps = 0
temp_var =0.0 #for swap purpose
ans = (low+high)/2
new_number = 0.0 #for negative integer purpose
epsilon = 0.01 # to check the accuracy
#if number<0:
##    temp_var = low
##    low = high
##    high = temp_var
#    while(abs(ans**3-number)>=epsilon):
#        steps += 1
#        if ans**3 < number:
#             low = ans
#        else: 
#            high = ans
#        ans = (low+high)/2.0
#else:
while abs(ans**3-number)>=epsilon:
     steps += 1
#     print (ans)
     if ans**3 > number:
         high = ans
     else:
         low = ans
     ans = (high+low)/2.0
print(steps)
print(ans)
            