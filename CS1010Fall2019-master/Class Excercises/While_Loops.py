# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:17:59 2019

@author: mushtu
"""
#Initialization of a counter variable
count = 0
#Specify Condition
while (count < 5): 
##Do something: Action
    print("Hello World") 
#Increment the counter
    count = count + 1












    
    
 ##Another example with else
y = 0
while y < 10:
    print('y is currently: ',y)
    print(' y is still less than 10, adding 1 to y')
#Alternate method of incrementing
    y+=1    
else:
    print('All Done!')  
    
    
  

    
    
    
    
    
    
    
##Bacteria Growth Rate
#Initialization
time=0
#Given
population = 1000
growth_rate= 0.21
while population < 2000:
    population = population + growth_rate*population
    print(population)
    time=time+1
print('For the population to double it takes ',time, 'minutes')
print('Final population is ', population)












##Continue statement
y = 0
while y < 5:
    print('y is currently: ',y)
    print(' y is still less than 5, adding 1 to y')
    y+=1
    if y==3:
        print('y==3')
    else:
        print('continuing...')
        continue    










    
##Break statement    
y = 0
while y < 5:
    print('y is currently: ',y)
    print(' y is still less than 5, adding 1 to y')
    y+=1
    if y==3:
        print('Breaking because y==3')
        break
    else:
        print('continuing...')
        continue    
       







        
##More examples
##Problem 1a
count=0
while True:
    count+=1
    if count>5:
        break
    print (count)
    














##Problem 1b    
count=0 
while count<10:
    count+=1
    if count%2 ==0:
        continue
    print (count)







##Census
census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
               5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
               8236, 17558, 17990, 18976, 19378 ]
sum_change = 0
i = 1
while i<len(census):
    pct = (census[i] - census[i-1]) / census[i-1] * 100
    sum_change += pct
    i += 1
print("Average = {:.1f}%".format( sum_change/(len(census)-1))) 


##Nested While
L = [2, 21, 12, 8, 5, 31]
i = 0
while i < len(L):
    j = 0
    while j < len(L):
        print(L[i], L[j])
        j += 1
    i += 1


























##Problem 1
l=[1,2,3,4,5,6,7,8,9,10,13,17]
i=0
even=0
odd=0
while i<len(l):
    if l[i] %2==0:
        even+=1
    else:
        odd+=1
    i+=1
print ('Even = ', even)
print ('Odd = ', odd)









##Problem 2
n1=[]
x=1500
while x in range(1500,2700):
    if (x%7==0) and (x%5==0):
        n1.append(str(x))
    x+=1
print (n1)














##Prime or not
num = 12 
# If given number is greater than 1 
if num > 1: 
#Initialize
   i=2      
   # Condition:Iterate from 2 to n / 2  
   while i <= num//2:          
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
       else:
#Increment
           i+=1
   else: 
       print(num, "is a prime number") 
else: 
   print(num, "is not a prime number") 



















##Printing Primes
##Read user input
##eval is another function that converts user provided input to a number
max_val=eval(input('Display Primes up to what value? '))
##Smallest prime number
value=2
while value<=max_val:
##Initialize a flag that stores the status of a number: prime or not
    is_prime=True
##Try all possible factors upto max_val
    trial_factor=2
    while trial_factor<value:
        if value%trial_factor==0:
            is_prime=False
            break
        trial_factor+=1
    else:
        print(value, end=' ')
    value+=1
print()




##Demonstrate end
print('My ')
print('Name ')
print('My ', end="")
print('Name ', end="")











##The star problem
##First Half
i=0
while i<5:
    j=0
    while j<=i:
      j+=1
##Don't let the line end until all stars printed
      print ('* ', end="")
    i+=1
    print('')  
       
    
#Second Half
i=i-1
while i>0:
    j=0
    while j<i:
        print ('* ', end="")
        j+=1
    i-=1
    print('')





















