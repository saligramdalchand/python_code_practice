#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:09:09 2018

@author: dc
"""

#this program is for finding the solution of a problem given on youtube
# x + y + z = 30 : where x,y,z can be 1, 3, 5, 7, 9, 11, 13, 15
count = 0
numbers= (1, 3, 5, 7, 9, 11, 13, 15)
for x in numbers:
    for y in numbers:
        for z in numbers:
            count += 1
            if x+y+z == 30:
                print (x,y,z)
                #break
                #print("trying")
#print (count)