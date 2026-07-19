a = 10;
b = 5;


# Comparison Operators

res = a == b;  # Equality Operator -- Returns True if two numbers are equal, False otherwise.
print(res);  # Prints the value of res which is False

res = a == 10;  # Equality Operator -- Returns True if two numbers are equal, False otherwise.
print(res);  # Prints the value of res which is True


res = a != b;  # Inequality Operator -- Returns True if two numbers are not equal, False otherwise.
print(res);  # Prints the value of res which is True

res = a != 10;  # Inequality Operator -- Returns True if two numbers are not equal, False otherwise.
print(res);  # Prints the value of res which is False



res = a > b;  # Greater Than Operator -- Returns True if the first number is greater than the second, False otherwise.
print(res);  # Prints the value of res which is True

res = a < b;  # Less Than Operator -- Returns True if the first number is less than the second, False otherwise.
print(res);  # Prints the value of res which is False

res = a >= b;  # Greater Than or Equal Operator -- Returns True if the first number is greater than or equal to the second, False otherwise.
print(res);  # Prints the value of res which is True

res = a <= b;  # Less Than or Equal Operator -- Returns True if the first number is less than or equal to the second, False otherwise.
print(res);  # Prints the value of res which is False



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

 
 # Bitwise Operators.    


