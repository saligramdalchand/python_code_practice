#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:38:06 2018

@author: dc
"""
#this program is made for the study of a function which is going to be the root**power

number = int(input('please provide a integer number to check for the logic\n'))

root = 0
x = 1
if root**x == abs(number):
    print('***')
else:
    while(root!=abs(number)):
        if root**x == abs(number):
            print('the solution of the problem number ',number,' is ',root,' to the power ', x)
            break
        elif root**(x+1) == abs(number):
            x=x+1
            print('the solution of the problem number ',number,' is ',root,' to the power ', x)
            break
        elif root**(x+2) == abs(number):
            x=x+2
            print('the solution of the problem number ',number,' is ',root,' to the power ', x)
            break
        elif root**(x+3) == abs(number):
            x=x+3
            print('the solution of the problem number ',number,' is ',root,' to the power ', x)
            break
        elif root**(x+4) == abs(number):
            x=x+4
            print('the solution of the problem number ',number,' is ',root,' to the power ', x)
            break
        else:
            root = root+1
        
if root == abs(number):
    print('the number',number,'did not have any square to the square value')

