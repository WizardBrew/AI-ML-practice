# if else statement.

x = 10;
# x = 20;
if x > 20:
    print("x is greater than 5");    #(spaces are important, its indentation, it define the scope of the code block.)

# it will print without else statement because x is greater than 5, if x was less than or equal to 5 then it will print the else statement.

else:
    print("x is less than or equal to 20"); 

print("This is outside the if else statement");  # This will print regardless, kyo ki  it is outside the if else statement.


# Lets create a program voter wala.

age = int(input("Enter your age: "))  #int kyo ki user input string me deta hai, to usko int me convert karna padta hai.

if age >= 18:
    print("You are eligible to vote.");  # agar age 18 se uppar ya 18 ke barabar hai to yeh print hoga.
else:
    print("You are not eligible to vote.");  #   (agar kuch unexpected of above hai toh yeh handle karega)



# thoda next level with elif statement. isko ladder bhi bolte hai. but its not best practice to use ladder if else statement, kyuki yeh code ko complex bana deta hai. isliye hum function ka use karte hai. 
# instead of elif dictationary, we can use function to make it more readable and maintainable. but for now lets see how ladder if else statement works.

checkResult = float(input("Enter your marks: "))

if checkResult >= 90:                   #(we can add isdigit in advance we see further -- remind me)
    print("You got A grade.");  # agar marks 90 se uppar ya 90 ke barabar hai to yeh print hoga.
elif checkResult >= 70 and checkResult < 90:
    print("You got B grade.");  # agar marks 70 se uppar ya 70 ke barabar hai aur 90 se chota hai to yeh print hoga.
elif checkResult >= 50 and checkResult < 70:
    print("You got C grade.");  # agar marks 50 se uppar ya 50 ke barabar hai aur 70 se chota hai to yeh print hoga.

else:
    print("You got D grade.");  # agar marks 50 se chota hai to yeh print hoga.  


#Homework: check gratest of two numbers using if else statement.
# check if the given number is + / - or null

# Tomorrow we can solve this again.

firstNumber = int(input('Enter the first number : '));
secondNumber = int(input('Enter second number: '));

if firstNumber > secondNumber:
    print('first number is greater', firstNumber);
elif firstNumber == secondNumber:
    print("They are equal to each other")
else:
    print('second number is greater', secondNumber);

# HW - Second Prog

if firstNumber > 0:
    print("entered number is positive");
elif firstNumber == 0:
    print("Number is zero or null");
else:
    print("Number is negative");



