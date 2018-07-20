#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:06:00 2018

@author: dc
"""

#this is after listening the lecture on edx
s = str(input('please provide the list of the decimal value with comma separated\n'))


#s = '1.23,2.4,3.123' 
length = len(s)
start = 0
count =0
summation = 0.0
for i in s:
    count = count+1    
    if i==',':
        summation = summation + float(s[start:count-1])
        start=count
summation = summation + float(s[start:length])
print ("the result of all the decimal number's sum is",summation)
#finallly i made it and the program runs very efficiently