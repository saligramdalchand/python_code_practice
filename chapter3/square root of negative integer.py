#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 18:10:38 2018

@author: dc
"""

#this is the finding of the square root of the number which is a negative integer

number = float(input('please provide the interger number of which you want to get square root\n'))
low = min(0,number) #these are just new trick of using min and max
high =max(0,number)
new_number = 0.0  #for stroing the positive number of the negative number
temp_var = 0.0   #for swaping value of low and high when number is negative
steps = 0
ans = (low + high)/2.0
epsilon = 0.01
# i am un necessarly writing this piece of code
#we can do this buy getting abs of number in starting
#and checking the result in last whether the number is negative or not
#by the way i am learning the hard coding 
#smile please 

if number < 0: #this will run if number is negative
    new_number = abs(number) #to get the positive value of number
    temp_var= low #swap
    low =high
    high = temp_var
    while abs(ans**2 - new_number) >= epsilon: #very similar loop as was expected for square root
        steps +=1
        if ans**2 > new_number:
            high = ans
        else:
            low = ans
        ans = (low+high)/2.0#i am not using abs in this place and its making result awesome
        
else:# this will run if number is positive
    while abs(ans**2 - number) >= epsilon: #this is also the same thing
        steps +=1
        if ans**2 > number:
            high = ans
        else:
            low = ans
        ans = abs(high + low)/2.0

#this piece of code is very awesome as i learnt the thing of swaping the result in the middle code
#
print('the number of steps followed in the whole calculations are',steps)

print (ans)