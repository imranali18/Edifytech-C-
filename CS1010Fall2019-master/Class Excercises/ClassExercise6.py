#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:10:18 2019

@author: uzma
"""
##Check if a number is positive, negative or zero
##Using if-elif ladder
def checknum(num):
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")













        
#Using Nested if
#num = float(input("Enter a number: "))
def checknum1(num):
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")
        








        
##Apple problem
def apple_buy(price, is_fresh):
    if is_fresh:
        if price<=5:
            return 'two dozen'
        else:
            return 'one dozen'
    return 'not fresh'
    
apple_buy(7,True)
apple_buy(2,False)













##Odd or even
def odd_even(enter_num):
    if enter_num >= 1 and enter_num <= 20: #conditional statement that ensures limit is between 1 and 20.
        print ("You have entered a valid number")
        if enter_num % 2 == 0: #test for even/odd
            print ("Your number is even")
            return (enter_num * enter_num)
        elif enter_num % 2 == 1: #test for even/odd
            print ("Your number is odd")
            return (enter_num * 3)
    else:
        print ("You've entered an invalid number")


odd_even(23)
odd_even(14)
odd_even(7)














##Alarm clock--Using Nested If
def alarm_clock(day, vacation):
  if vacation:
    if day==0 or day==6:
      return 'off'
    else:
      return '10:00'
  else:
    if day==0 or day==6:
      return '10:00'
    else:
      return '7:00'
  
alarm_clock(1, False)
alarm_clock(5, True)
alarm_clock(0, False)
alarm_clock(0, True)






    
##Date problem
      
def date_fashion(you, date):
    if you<=2 or date<=2:
        return 0
    elif you >=8 or date >=8:
        return 2
    else:
        return 1


date_fashion(5, 10) 
date_fashion(5, 2)
date_fashion(5, 5)




