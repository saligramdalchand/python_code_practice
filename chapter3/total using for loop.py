#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:34:00 2018

@author: dc
"""

#doing total with for loop

number = int(input('please provide the number upto which you want to get total\n'))
total =0
for c in range(number):
    total = total+c
print ('the sum of number',number,'is',total)