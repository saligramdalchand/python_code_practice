#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 19:44:11 2018

@author: dc
"""

s = 'abcdefghiiijjkkklmnascdfe'
r = ' ' 
c = ' '
for char in s:
    if char == ' ' or char < c[-1]:
        c = char
    elif char >= c[-1]:
        if c[-1] == ' ':
            c = char       
        elif char == c[-1] or ord(char) == ord(c[-1])+1:
            c += char
        if len(r) < len(c):
                r = c
print (c)
print (r)
print(len(r))