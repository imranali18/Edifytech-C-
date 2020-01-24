# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:36:53 2019

@author: mushtu
"""

L=[1,1,2,3,4,5,1]
L.count(1)


#Remove common elements
set_x = set(["a", "b","c"])
set_y = set(["b", "d","f"])
set_c = set_x ^ set_y
print(set_c)


list1=[1,2,3,4,5,6,6,6]
new=set(list1)
new
print(sum(new)/len(new))



M = ['a', 'b', 'c']  
print ("Element = ",(M[3]))





def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)


arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")





fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print (sum)



def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))



def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))



L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)



fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
print (len(fruit))


def new():
    arr = {}
    arr[1] = 1
    arr['1'] = 2
    arr[1] += 1
    sum = 0
    for k in arr:
        sum += arr[k]
    return (sum)

new()


init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print (init_tuple_a == init_tuple_b)




a = {'a':1,'b':2,'c':3}
b = {'b':2,'a':1,'c':3}
a!=b


def countdict():
    from collections import Counter
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    d = Counter(d1) + Counter(d2)
    return (d)

countdict()


def ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(ends('w3resource'))



x={1,2,3,4,4,3,1,1,1,2,2}
y={1,2,3,4}
x!=y



fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list1
fruit_list2 = fruit_list1
fruit_list2
fruit_list3 = fruit_list1[:]
fruit_list3
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

fruit_list1, fruit_list2, fruit_list3


list1=[1,2,3]
list2=list1
list2
list2[1]=4
list2
list1
