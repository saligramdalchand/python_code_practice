#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:11:17 2018

@author: dc
"""

''' this is isIn function to find out the string is present in this or not'''
def isIn(a, b):
    if a in b:
        print ('string '+a+' is present in the string '+b)
        return True
    elif b in a:
        print('string '+b+' is present in the string '+a)
        return True
    else:
        print('none of them is present in each other')
        return False

string1 = input('give me first string: ')
string2 = input('give me second string: ') 
compare = isIn(string1, string2)
print (compare)       