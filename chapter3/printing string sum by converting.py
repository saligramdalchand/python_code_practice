#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 22:27:39 2018

@author: dc
"""

#this is the finger exersize from book for making the things the way book wants seperate the string 
#data in to integer and then use it in sum process

s = '1.23,2.4,3.123'
sum = 0
number=int(s)
for i in number:
    sum = sum + i
print (i)