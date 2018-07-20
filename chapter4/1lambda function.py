#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:10:02 2018

@author: dc
"""

        
""" lets get familier with lambda"""
"""map() and filter() are the iterative function that works for the list object"""

value = 5
double = lambda x: x*2


first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_first_list = list(filter(lambda x: x%2 == 0, first_list))
new_second_list = list(map(lambda x: x*7, first_list))
print (new_second_list)
print (double(new_second_list[5]))
print(new_first_list)