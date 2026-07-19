#Oprators


a = 10;
b = 5;

res = a + b;  # Addition Operator -- Adds two numbers and returns the result.
print(res);  # Prints the value of res which is 15

res = a - b;  # Subtraction Operator -- Subtracts two numbers and returns the result.
print(res + 5);  # Prints the value of res which is 5

res = a * b;  # Multiplication Operator -- Multiplies two numbers and returns the result.
print(res);  # Prints the value of res which is 50

res = a / b;  # Division Operator -- Divides two numbers and returns the result.
print(res);  # Prints the value of res which is 2.0

print(int(res));  # Prints the value of res which is 2  

res = a // b;  # Floor Division Operator -- Divides two numbers and returns the largest integer less than or equal to the result.
print(res);  # Prints the value of res which is 2


res = a ** 2;  # Exponentiation Operator -- Raises a number to the power of another number and returns the result.
print(res);  # Prints the value of res which is 100000

res = a % 3;  # Modulus Operator -- Divides two numbers and returns the remainder.
print(res);  # Prints the value of res which is 0


#Bodmas Rule -- Brackets, Order, Division, Multiplication, Addition, Subtraction. it solves the brackets first, then the order of operations, then division and multiplication from left to right, and finally addition and subtraction from left to right.

bodmas = (a + b * 2);  # Prints the value of a + b * 2 which is 20 -- Operator Precedence
# bodmas  = (a + b) * 2;  # Prints the value of (a + b) * 2 which is 30 -- Operator Precedence
# bodmas = (a + b) * 2 - 5;  # Prints the value of (a + b) * 2 - 5 which is 25 -- Operator Precedence ==> 15 * 2 - 5 = 30 - 5 = 25 | theek hai? 
print(bodmas);  # Prints the value of bodmas which is 20    
