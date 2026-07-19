a = 10;
b = 5;

# Logical Operators

res = a > 5 and b < 2 and 15 == 15;   # Logical AND Operator -- Returns True if both numbers are true, False otherwise.
print(res);  # Prints the value of res which is False             (if all res are true then it will return true otherwise false) 

res = a > 5 and b < 10;  # Logical AND Operator -- Returns True if both numbers are true, False otherwise.
print(res);  # Prints the value of res which is True               (if anyone res is false then it will return false.)  | Clear till here?


res = a > 5 or b > 10;  # Logical OR Operator -- Returns True if at least one of the numbers is true, False otherwise.
print(res);  # Prints the value of res which is True             (yeh opposite hai AND ka, agar koi bhi res true hoga to yeh true return karega otherwise false.)

res = not (a > 5);  # Logical NOT Operator -- Returns True if the number is false, False otherwise.
print(res);  # Prints the value of res which is False            (yeh opposite hai, agar res true hoga to yeh false return karega otherwise true.)

res = not (a == 10);  # Logical NOT Operator -- Returns True if the number is false, False otherwise.
print(res);  # Prints the value of res which is False            (yeh opposite hai, agar res true hoga to yeh false return karega otherwise true.)

res = not (a != 10);  # Logical NOT Operator -- Returns True if the number is false, False otherwise.
print(res);  # Prints the value of res which is True            (yeh opposite hai, agar res true hoga to yeh false return karega otherwise true.)

# till here all clear? Tomorrow we will learn about Bitwise Operators. Homework use it in samll cases and expalin it to me.

 
 # Assignment Operators.

a = 10;  # Assigns the value of 10 to the variable a.
a += 5;  # Adds 5 to the value of a and assigns the result back to a. Equivalent to a = a + 5.
          # this is something like a = 10 + 5;  # Assigns the value of 15 to the variable a.         (dono same hai, dono ka output same hoga.)

a = a+5;  # Adds 5 to the value of a and assigns the result back to a. Equivalent to a = a + 5.     (ab is ka output 20 hoga, kyuki pehle a = 15 tha, ab a = 15 + 5 = 20 hoga.)

print(a);  # Prints the value of a which is 20              

a+= 10;  # Adds 10 to the value of a and assigns the result back to a. Equivalent to a = a + 10.        (only existing variable can be used in this case, otherwise it will give an error.) 

print(a);  # Prints the value of a which is 30


b = 20;  # Assigns the value of 20 to the variable b.
b -= 5;  # Subtracts 5 from the value of b and assigns the result back to b. Equivalent to b = b - 5.

b -=9;  # Subtracts 9 from the value of b and assigns the result back to b. Equivalent to b = b - 9.

print(b);  # Prints the value of b which is 6


a *= 2;  # Multiplies the value of a by 2 and assigns the result back to a. Equivalent to a = a * 2.
print(a);  # Prints the value of a which is 60

b /= 2;  # Divides the value of b by 2 and assigns the result back to b. Equivalent to b = b / 2.
print(b);  # Prints the value of b which is 3.0
print(int(b));  # Prints the value of b which is 3


c =70;
# the below line will give an error because c is not defined before this line. So, we need to define c before using it in the assignment operator.
c //= 2;  # Floor divides the value of c by 2 and assigns the result back to c. Equivalent to c = c // 2.
print(c);  # Prints the value of c which is 35


#this is error c cannot be used with new variable, it can only be used with existing variable. So, we need to define c before using it in the assignment operator.

# res = c//=2;  # Floor divides the value of c by 2 and assigns the result back to c.     (can use Equivalent to c = c // 2.)
print(res);  # Prints the value of res which is 17


#bitwise Operators  >> Skipping this for now,  just with one example.
''' 
0  = 0000000000000000
1  = 0000000000000001
2  = 0000000000000010
3  = 0000000000000011
4  = 0000000000000100
5  = 0000000000000101
6  = 0000000000000110
7  = 0000000000000111
8  = 0000000000001000
9  = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
13 = 0000000000001101
14 = 0000000000001110
15 = 0000000000001111  '''


a = 10;  # Assigns the value of 10 to the variable a.
b = 5;   # Assigns the value of 5 to the variable b.
res = a &  b;  # Bitwise AND Operator -- Performs a bitwise AND operation on two numbers and returns the result.
print(res);  # Prints the value of res which is 0  (10 in binary is 1010 and 5 in binary is 0101, so the result of 1010 & 0101 is 0000 which is 0 in decimal.)
#however, if we take a = 10 and b = 2, then the result will be 2 because 10 in binary is 1010 and 2 in binary is 0010, so the result of 1010 & 0010 is 0010 which is 2 in decimal.  reference: https://www.w3schools.com/python/python_operators.asp


res = a | b;  # Bitwise OR Operator -- Performs a bitwise OR operation on two numbers and returns the result.
print(res);  # Prints the value of res which is 15  (10 in binary is 1010 and 5 in binary is 0101, so the result of 1010 | 0101 is 1111 which is 15 in decimal.)     it takes value of a and b then checks value of a and b then if any of the value is 1 then it will return 1 otherwise 0.  reference: https://www.w3schools.com/python/python_operators.asp
