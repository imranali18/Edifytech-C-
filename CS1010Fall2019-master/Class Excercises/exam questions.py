# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 08:46:14 2019

@author: mushtu
"""

# Function to demonstrate printing pattern triangle 
def test(n): 
      
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\n") 
  
# Driver Code 
n = 5
test(n) 


    # 10 is the total number to print
    for num in range(10):
        for i in range(num):
            print (num, end=" ") #print number
        # new line after each row to display pattern correctly
        print("\n")
        
        
    
    lastNumber = 6
    for row in range(1, lastNumber):
        for column in range(1, row + 1):
            print(column, end=' ')
        print("")
        
        
Number = 6
for row in range(1, Number):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
    
    
    
rows=6    
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\n")
    
    
rows = 4
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\n")
for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\n")
    
    
l=[10,2,3,4,5]
a=0
for i in range(0,len(l)):
    a=a+l[i]
print('Average =', a/len(l))



L = [1,2,3]
i = 0
while i < len(L):
    j = 0
    while j < len(L):
        print(L[i], L[j])
        j += 1
    i += 1
    
    
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grapes')
fruits.sort()
fruits
fruits.remove('apple')
fruits


l1=[1,5,-1,-3]
l2=[2,6,-7,0]
for i in range(len(l1)):
    l2[i]=l1[i+1]
    
    
    
    
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def list_fact(y):
    final=[]
    for i in range(len(y)):
       final.append(fact(y[i]))
    print(final)
    
list_fact([2,5,1])


def square_num(x):
    final=[]
    for i in range(0,len(x)):
        final.append((x[i])**i)
    print(final)

square_num([1,2,3,4,5])

def odd_num(x):
    l1=[]
    for i in range(len(x)):
        if x[i]%2==0:
            continue
        l1.append(x[i])
    print(l1)

odd_num([1,3,7,8,10])



    # 10 is the total number to print
    for num in range(5):
        for i in range(num):
            print (num, end=" ") #print number
        # new line after each row to display pattern correctly
        print("\n")
