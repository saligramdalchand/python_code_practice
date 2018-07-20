#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:47:57 2018

@author: dc
"""

def isPalindromic(s):
    """this program accept s as string 
    if s is paindromic then it returns True else returns False
    any special character or case is ignores that is no case sensitive """
    def char(s):
        print('this is in char corner '+s)
        s=s.lower()
        letter = ''
        for i in s:
            if i in ('abcdefghijklmnopqrstuvwxyz'):
                letter += i
        return letter
    def isPal(s):
        print('this is in the isPal corner '+s)
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(char(s))

print(isPalindromic('te!@#@$$#%#%$%&(*)jukpapk12!@#!@$ujet43768432 @#$325325'))