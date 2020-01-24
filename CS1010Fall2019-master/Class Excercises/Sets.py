# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:58:30 2019

@author: mushtu
"""
##Define a set
{1+2, 3, "a"}
{2,1,3}
#Alternate
new_set=set([1,2,2,2,2,3])
print(new_set)















##Cardinality of a set=no. of distimct elements
len({'a', 'b', 'c', 'a', 'a'})













# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
##Empty set
set()











##Summing
sum({1,2,3})
sum({1,2,3}, 10)












##testing Set Membership
S={1,2,3}
2 in S
4 in S
4 not in S













##Union and Intersection
a={0,1,2,3}
b={0,2,3,4} 
a|b
a & b
{1,2,3,5} | {2,3,4,5,6}    ##Union
{1,2,3} & {2,3,4}    ##Intersecton
{-1,-2,1,2,3,5} ^ {-1,-2,-3,2,3,4,5,6}

















##Alternate method
people = {"Jay", "Id", "Arch","Joe"}
vampires = {"Kar", "Joe"}
population = people.union(vampires)
population

victims = people.intersection(vampires)
victims


##Difference method
safe = people.difference(vampires)
safe







##Clear method
victims.clear()
victims














##Symmetric difference
m={1,3,5}
n={1,2,3}
print(m.symmetric_difference(n))












##Mutating a Set
S={1,2,3}
S.add(4)
S
S.remove(2)
S
S.update({4, 5, 6})
S
S.intersection_update({5,6,7,8,9})
S



















##Multiple variable Same Set
T=S
T.remove(5)
T
S
















##Copying
U=S.copy()
print(U)
U.add(5)
S















##Another example
first = {'g', 'e', 'e', 'k', 's'} 
second = first.copy() 
print(second)
second.remove('s')
print(second)
print(first)














##Set comprehensions
#Notice the braces: Different from list comprehensions
{2*x for x in {1,2,3} }

{x for x in {'a','b','c'}}













S={1,2,3}
##Union
{x*x for x in S | {5, 7}}















##if condition
{x*x for x in S | {5, 7}  if x > 2}
















##Cartesian product of two sets
{x*y for x in {1,2,3} for y in {2,3,4}}














##With filter --Look at this again
{x*y for x in {1,2,3} for y in {2,3,4} if x != y}












##pop 
s={1,2,3,4,5}
s.pop()
s
