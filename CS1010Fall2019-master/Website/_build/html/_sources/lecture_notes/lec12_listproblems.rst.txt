Lecture 12 --- Solving Problems on Lists
========================================

In today's lecture we solve a few problems on lists to understand the concept of lists better.

Overview of Today
-----------------

-  List functions and Methods

-  Nested lists OR

-  Lists of lists


Additional Methods
------------------

Today we will also talk about a few more methods that work on lists and strings:

Converting Strings to Lists
---------------------------

-  Method 1: use function :func:`list` to create a list of the
   characters in the string.

-  Method 2:  use the string :func:`split` function, which breaks a string up into a
   list of strings based on the character provided as the argument.

   -  The default is ``' '``.

   -  Other common splitting characters are ``','``, ``'|'`` and
      ``'\t'``.

-  We will explore with the ``s = "Hello world"`` example in class.
   

Converting Lists to Strings
---------------------------

-  What happens when we type the following?

   ::

       >>> s = "Hello world"
       >>> t = list(s)
       >>> s1 = str(t)
       

   This will not concatenate all the strings in the list (assuming they are
   strings).

-  We can write a ``for`` loop to do this, but Python provides
   something simpler that works: 

   ::

     >>> L1 = ['Hello', 'World']
     >>> print(''.join(L1))
     HelloWorld
     >>> print(' '.join(L1))
     Hello World


Lecture Slides:
---------------

https://drive.google.com/file/d/1s6mYxt_wSDXdTGUmihHJtrFkxfWT9li2/view?usp=sharing




