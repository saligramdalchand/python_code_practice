#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 16:01:20 2018

@author: dc
"""


    
    
"""
    this program is to know that how the values are assign to the function and the power of stacking of a
    function. the way all the variables get occupies their places 
"""
def f(x):                        
        def g():
            x = 'abc'
            print('x =', x)
        def h():
            z = x
            print('z =', z)
        x = x + 1
        print('x =', x)
        h()
        g()
        print('x =', x)
        return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()