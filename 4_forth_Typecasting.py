
name = "Wizard"  # Variable name is a string
age = 35  # Variable age is an integer


print('My name is',name,'and I am ' + str(age) + ' years old.')  # Concatenating strings and converting age to string

print(f"My name is {name} and I am {age} years old.")  # Using f-string for formatted output

experience = input('I have been working for : ')
print(type(experience))  # Displaying the type of the input variable

experience = int(experience)  # Converting the input string to an integer
print(type(experience))  # Displaying the type of the variable after conversion

output = (f"My name is {name}, I am {age} years old, and I have {experience} years of experience.")  # Using f-string for formatted o

print(output)  # Printing the final output
print(type(output))  # Displaying the type of the output variable
