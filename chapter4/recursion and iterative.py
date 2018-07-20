#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:16:33 2018

@author: dc
"""

# this program is for the finding of the factoriall of a number by using iterative method and recursive method
#i am very glad that this i learnt the things that i did not thought about in the post graduation.
#thank you python

#iterative search

def FactI(n):
    """this program accept n int >0 
    it returns result as factorial of n """
    result = 1
    if n < 1:
        return n
    while(n>1):
        result = n * result
        n -= 1
    return result

#recursive search
    
def FactR(n):
    """this program accept n int > 0
    it returns result as factorial of n"""
    if n == 1:
        return n
    else:
        return n*FactR(n-1)
    
print(FactR(-98))
print(FactI(-98))