#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:33:08 2018

@author: dc
"""

#this program is for finding the fibonacci and testing the fibonacci by using the recursive method

#lets do it

def Fibo(n):
    """this program accept n int > 0
    it returns fibonacci of the number n """
    if n == 1 or n == 0:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)
def TestFibo(n):
    for x in range(n+1):
        print("fibonacci of x =",x, "is ",Fibo(x))

TestFibo(20)