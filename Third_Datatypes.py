#DataTypes

#Integer
from xmlrpc.client import boolean


a = 10;   #Numbers from -infinity to +infinity are considered as Integers in Python.
print(type(a));  # Prints the type of a which is <class 'int'>
print(a);  # Prints the value of a which is 10

#float
b = 10.54321;  # Numbers with decimal points are considered as Floats in Python.
print(type(b));  # Prints the type of b which is <class 'float'>
print(b);  # Prints the value of b which is 10.54321

bb = 10/5; # Division of two integers results in a float in Python.
print(type(bb));  # Prints the type of bb which is <class 'float'>
print(bb);  # Prints the value of bb which is 2.0 

#Complex datatype.
c = 10 + 5j;  # Numbers with a real and imaginary part are considered as Complex numbers in Python.
print(type(c));  # Prints the type of c which is <class 'complex'>
print(c);  # Prints the value of c which is (10+5j)

#string datatype.
string = "Hello World cloud9 #instafollowers 'Gamers challenge on 4/08/2026' ";  # A sequence of characters is considered as a String in Python.
print(type(string));  # Prints the type of string which is <class 'str'>  
print(string);  # Prints the value of string

#boolean datatype.
boolean_a = True;  # A boolean value can be either True or False in Python.
boolean_b = False;  # A boolean value can be either True or False in Python.
print(type(boolean_a));  # Prints the type of boolean_a which is <class 'bool'>
print(type(boolean_b));  # Prints the type of boolean_b which is <class 'bool'>

print(boolean_a);  # Prints the value of boolean_a which is True
print(boolean_b);  # Prints the value of boolean_b which is False

#none datatype.
none = None;  # None is a special constant in Python that represents the absence of a value or a null value.
print(type(none));  # Prints the type of none which is <class 'NoneType'>
print(none);  # Prints the value of none which is None.

