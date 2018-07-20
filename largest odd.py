#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:51:53 2018

@author: dc
"""
"""
Title : finding the largest odd from the given set of 10 numbers
"""
first = int(input("Print the number you want to check for biggest odd from the list\nfirst number : "))
second = int(input("\nSecond number : "))
third = int(input("\nThird number : "))
forth = int(input("\nforth number : "))
fifth = int(input("\nfifth number : "))
sixth = int(input("\nsixth number : "))
seventh = int(input("\nseventh number : "))
eighth = int(input("\neighth number : "))
ninth = int(input("\nninth number : "))
tenth = int(input("\ntenth number : "))
a = [first, second, third, forth, fifth, sixth, seventh, eighth, ninth, tenth]
LargestNum = 0
x = 0
while (x<10):
    if a[x]%2 == 0:
        print ('***')
    elif a[x]>LargestNum:
        LargestNum = a[x]
    x =x+1
if LargestNum == 0:
    print ("there is no number which is odd in the list")
else:
    print("the largest odd from the given numbers is ", LargestNum)
