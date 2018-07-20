#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:33:12 2018

@author: dc
"""

#this program is for the global variable uses
#global and the fibonacci are used

def Fib(n):
    global timesFibCalls
    timesFibCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)


def testFib(n):
    for i in range(n+1):
        global timesFibCalls
        timesFibCalls = 0
        print ('fib of',i,'=',Fib(i))
        print('fib called',timesFibCalls,'times.')
        
testFib(6)
