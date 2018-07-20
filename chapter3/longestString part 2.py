#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:05:13 2018

@author: dc
"""
s = 'gdnwvyexwwqxefpylnx'
r = ' ' 
c = ' '
for char in s:
    if char == ' ' or char < c[-1]:
        c = char
    elif char >= c[-1]:
        if c[-1] == ' ':
            c = char       
        elif char == c[-1] or ord(char) > ord(c[-1]):
            c += char
            if len(r) < len(c):
                r = c
if r == ' ':
    r = s[0]
print('Longest substring in alphabetical order is:',r)