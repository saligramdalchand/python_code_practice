#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:58:18 2018

@author: dc
"""

#this program is to understand the functioning of for loop
''''
x = 5
for i in range(x):
    print (i)
'''
'''
x = 5
for i in range(x):#this means that the value of the range get fixed as it get the value of x .
    print (i)
    x = 3
'''


x = 5
for j in range(x):     #here the value of the range get to the 0-4 and this goes 0 to 4 times
    for i in range(x):   #here the value of the 
        print (j)
        x =2
#the thing that i am understanding from this all the code is that value of j get fixed 
#then value of i and the value is going to change if and only if when the loop get over and
#new value is going to assign to the for loop
'''
result will be
0
0
0
0
0
1
1
2
2
3
3
4
4
this suggest that iteration will not change the value untill its get completly exhaust
   ''' 