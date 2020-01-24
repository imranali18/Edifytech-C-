Lecture 9 — Tuples, Modules, and Images
=======================================

Overview
--------

-  While most of this lecture is not covered in our textbook, this
   lecture serves as an introduction to using more complex data types
   that are iterables. WE are familiar with one iterable - string.

-  We will first learn a simple data type called tuples which allow
   us to work with multiple values together - including returning two
   or more values from a function.

-  We will then revisit modules, how functions you write can be used
   in other programs.

-  Most of the class we will be learning how to use a new module for
   manipulating images.

   - We will introduce a new data type - an image - which is much more
     complex than the other data types we have learned so far.

   - We will study a module called *pillow* which is specifically
     designed for this data type.


Tuple Data Type
---------------

-  A *tuple* is a simple data type that puts together multiple values 
   as a single unit.

-  A tuple allows you to access individual elements:
   first value starts at zero (this "indexing" will turn into a big
   Computer Science thing!):

   ::

       >>> x = (4, 5, 10)   # note the parentheses
       >>> print(x[0])
       4
       >>> print(x[2])
       10
       >>> len(x)
       3

-  As we will explore in class tuples and strings are similar in many
   ways:

   ::

       >>> s = 'abc'
       >>> s[0]
       'a'
       >>> s[1]
       'b'

-  Just like strings, you cannot change a part of the tuple; you can
   only change the entire tuple:


Basics of modules
------------------

-  Recall that a module is a collection of Python variables, functions
   and objects, all stored in a file.

-  Modules allow code to be shared across many different programs.

-  Before we can use a module, we need to import it.  The import of a
   module and use of functions within the module have the follow
   general form:

   ::

       >>> import module_name
       >>> module_name.function(arguments)


PIL/PILLOW — Python Image Library
----------------------------------

-  PILLOW is a series of modules built around the ``Image`` type, our first
   object type that is not part of the main Python language.

   -  We have to tell Python about this type through ``import``.

-  We will use images as a continuing example of what can be done in
   programming beyond numbers and beyond text.

-  See 

   http://pillow.readthedocs.org/en/latest/handbook/tutorial.html

   for more details.


Lecture Slides
--------------

https://drive.google.com/file/d/1xU4AHGrXtGvgEERL1ptdC0ucMWFLPxos/view?usp=sharing

Lecture Videos
--------------

https://www.youtube.com/watch?v=vEsHRpBSYcE

https://www.youtube.com/watch?v=t89rXySnUmU

