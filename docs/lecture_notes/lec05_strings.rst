Lecture 5 — Strings
===============================================

In this Chapter
---------------

In this chapter we will explore strings. We are going to explain how they are implemented in C# 
and in what way we can process text content. Additionally, we will go through different methods 
for manipulating a text: we will learn how to compare strings, how to search for substrings, how
to extract substrings upon previously settled parameters and last but not least how to split a 
string by separator chars. We will demonstrate how to correctly build strings with the StringBuilder 
class. We will provide a short but very useful information for the most commonly used regular 
expressions. We will discuss some classes for efficient construction of strings. Finally, we will take 
a look at the methods and classes for achieving more elegant and stricter formatting of the text 
content 

What Is a String? 
-----------------

A string is a sequence of characters stored in a certain address in memory. Remember the type char?
In the variable of type char we can record only one character. Where it is necessary to process more 
than one character then strings come to our aid. In. NET Framework each character has a serial number
from the Unicode table. The Unicode standard is established in the late 80s and early 90s in order to
store different types of text data. Its predecessor ASCII is able to record only 128 or 256 characters 
(respective ASCII standard with 7-bit or 8bit table). Unfortunately, this often does not meet user needs
– as we can fit in 128 characters only digits, uppercase and lowercase Latin letters and some specific 
individual characters. When you have to work with text in Cyrillic or other specific language 
(e.g. Chinese or Arabian), 128 or 256 characters are extremely insufficient. 
Here is why .NET uses 16-bit code table for the characters. With our knowledge of number systems and 
representation of information in computers, we can calculate that the code table store 2^16 = 65,536 
characters. Some characters are encoded in a specific way, so it is possible to use two characters of 
the Unicode table to create a new character – the resulting signs exceed 100,000. 

The System.String Class 
-----------------------

The class System.String enables us to handle strings in C#. For declaring the strings we will continue 
using the keyword string, which is an alias in C# of the System.String class from .NET Framework. The 
work with string facilitates us in manipulating the text content: construction of texts, text search and
many other operations. Example of declaring a string: 


::

       string greeting = "Hello, C#"; 

We have just declared the variable greeting of type string whose content is the text phrase "Hello, C#". 
The representation of the content in the string looks closely to this: 

H e l l o ,  C # 

The internal representation of the class is quite simple – an array of characters. 
We can avoid the usage of the class by declaring a variable of type char[] and fill in the array’s 
elements character by character. However, there are some disadvantages too:
1. Filling in the array happens character by character, not at once.
2. We should know the length of the text in order to be aware whether it will fit into the already allocated space for the array.
3. The text processing is manual. 

Strings – Simple Example 
------------------------

Let’s give an example for using variables from the type string: 

::

       string message = "This is a sample string message."; 
 
       Console.WriteLine("message = {0}", message); 
       Console.WriteLine("message.Length = {0}", message.Length); 
       for (int i = 0; i < message.Length; i++) 
       {  
              Console.WriteLine("message[{0}] = {1}", i, message[i]); 
       }
              // Console output: 
              // message = This is a sample string message. 
              // message.Length = 31 
              // message[0] = T 
              // message[1] = h 
              // message[2] = i 
              // message[3] = s 
              // … 


Please note the string value – the quotes are not part of the text, they are enclosing its value. The 
example demonstrates how to print a string, how to extract its length and how to extract the character
from which it is composed. 

Declaring a String 
------------------
We can declare variables from the type string by the following rule: 

::
       string str; 

Declaring a string represents a variable declaration of type string. This is not equivalent to setting 
a variable and allocating memory for it! With the declaration we inform the compiler that the variable 
str will be used and the expected type for it is string. We do not create a variable in the memory and 
it is not available for processing yet (value is null, which means no value). 



Creating and Initializing a String 
----------------------------------

In order to process the declared string variable, we must create it and initialize it. Creating a 
variable of certain class (also known as instantiating) is a process associated with the allocation
of the dynamic memory area (the heap). Before setting a specific value to the string, its value is null.
This can be confusing to the beginner programmers: uninitialized variables of type string do not contain
empty values, it contains the special value null – and each attempt for manipulating such a string will 
generate an error (exception for access to a missing value NullReferenceException)! We can initialize 
variables in the following three ways: 

1. By assigning a string literal
2. By assigning the value of another string
3. By passing the value of an operation which returns a string


Setting a String Literal 
------------------------

Setting a string literal means to assign a predefined textual content to a variable of type string. We
use this type of initialization, when we know the value that must be stored in the variable. Example for
setting a string literal: 

:: 
       string website = "http://www.wikipedia.org"; 

In this example we created the variable website with value the above stated string literal. 


Assigning Value of Another String 
---------------------------------

Assigning a value is equivalent to directing a string value or a variable to a variable of type string.
An example is the following code snippet: 
::

       string source = "Some source"; 
       string assigned = source; 

First, we declare and initialize the variable source. Then the variable assigned takes the value of source.
Since the string class is a reference type, the text "Some source" is stored in the dynamic memory (heap)
on an address defined by the first variable. 
 
In the second line we redirect the variable assigned to the same place, which the other variable points to.
In this way the two objects receive the same address in dynamic memory and hence the same value. 
The change of either variable will affect only itself because of the immutability of the type string,
as when a change occurs, a copy of the changed string will be created. This is not true for the rest of
the reference types (the normal, mutable types) because with them the changes are made directly in the 
address in memory and all references point to this changed address.  

Passing a String Expression 
---------------------------
The third option to initialize a string is to pass the value of a string expression or operation, which 
returns a string result. This can be a result from a method, which validates data; adding together the 
values of a number of constants and variables; transforming an existing variable, etc. Example of an 
expression, which returns a string:

::
       string email = "some@gmail.com"; 
       string info = "My mail is: " + email; 
       // My mail is: some@gmail.com 
The info variable has been created from the concatenation of literals and a variable.



More Than Just Numbers
----------------------

-  Strings are our fourth type, after integers, floats and Boolean.

-  We’ve already seen the use of strings in output: 

   ::

       print("Hello world")
       x = 18
       y = 11
       print("Value of x is", x, "value of y is", y)


Topics for Today
----------------

-  String basics

-  String operations

-  Print formatting

Strings — Definition
--------------------

-  A string is a sequence of 0 or more characters delimited by single
   quotes or double quotes:

   ::

         'Rensselaer'
         "Troy, NY"
         '41 18 154 23 402'
         ''

Lecture Notes
--------------

https://drive.google.com/file/d/1KiOxGH1iYglVgfliAtyqoTaC_Kp0BQwN/view?usp=sharing

Lecture Videos
---------------
https://www.youtube.com/watch?v=bExECbKfOXM

https://www.youtube.com/watch?v=OhPyQ74AOzQ