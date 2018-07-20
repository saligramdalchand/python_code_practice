#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:48:06 2018

@author: dc
"""
#import time
#this is a megical program that is going to print the value same as the user
low = 0
high  = 100
magical_number = (low+high)/2
character = ' ' 
checker = ' '
print ('Please think of a number between 0 and 100!')
#time.sleep(5)
#print("there are some rule that you have to follow while going through it.")
#time.sleep(5)
#print("first and last rule")
#time.sleep(3)
#print("you have to enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
#time.sleep(6)
#print ("Is your secret number",magical_number,"?")
#print ("Enter 'h' to indicate the guess is too high.") 
#print("Enter 'l' to indicate the guess is too low.")
#print("Enter 'c' to indicate I guessed correctly.")


while (checker != 'c'):
    print("Is your secret number",magical_number,"?")
    character = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    checker = character
    if character == 'h':
        high = magical_number
    elif character == 'l':
        low = magical_number
    elif (checker == 'c'):
        break
    else:
        print("Sorry, I did not understand your input.")
    magical_number = int((low+high)/2)
    
if (checker == 'c'):
    print("Game over. Your secret number was:",magical_number)
else:
    print("tough choice\n")