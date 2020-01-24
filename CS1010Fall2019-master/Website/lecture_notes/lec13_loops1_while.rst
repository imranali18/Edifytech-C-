Lecture 13 — While Loops
===========================

Overview
--------

-  Loops are used to access and modify information stored in lists and
   are used to repeat computations many times.

-  We construct loops using logical conditions: ``while`` loops.

-  We will investigate single and multiple loops.

Reading:  Our coverage of loops is in a different order than that of
*Practical Programming*.  A direct reference for reading material is
Section 9.6.


Part 1: The Basics
------------------

-Iteration means executing the same block of code over and over many times. 

- A programming structure that implements iteration is called a loop.

- In programming, there are two types of iteration, indefinite and definite:

    With indefinite iteration, the number of times the loop is executed isn’t specified explicitly in advance. Rather, the designated block is executed repeatedly as long as some condition is met. For example While Loops.

    With definite iteration, the number of times the designated block will be executed is specified explicitly at the time the loop starts. For example for loop.


-  We will see two ways to write loops: using ``while`` loops and ``for`` loops.

-  In Python, ``while`` loops are more general because you
   can always write a ``for`` loop using a ``while`` loop.

-  We will start with ``while`` loops first and then see how we can 
   simplify common tasks with ``for`` loops later.


Basics of While
---------------

-  Our first ``while`` loop just counts numbers from 1 to 9, and prints them:

   ::

       i = 1
       while i < 10:
           print(i)
           i += 1   ## if you forget this, your program will never end

-  General form of a ``while`` loop:

   ::

       block a
       while condition:
           block b
       block c

-  Steps:

   #. General Procedure:
1. Initialize a counter variable
2. Specify the condition for while
3. Specify the required actions
4. Increment or Decrement the counter


Using Loops with Lists
-----------------------

-  Often, we use loops to repeat a specific operation on every element of
   a list.

-  We must be careful to create a number that will serve as the index
   of elements of a list. Valid values are: 0 up to (not including)
   the length of list:


  

Lecture Slides
-----------------------
   
https://drive.google.com/file/d/1Eol1pULgv2FBDY2A5dyEcaADgRX91zzE/view?usp=sharing



Lecture Video
-----------------------
https://www.youtube.com/watch?v=pBjdSIyUJR8&t=396s

