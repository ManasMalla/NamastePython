#Importing the math library
import math

#Input from user
userInput = input("Enter any input: ")
print("You just entered: {}\n".format(userInput))

#Understanding the format() operator
print("Age: {}, Salary: {}, Today: {}\n".format(30, 50000.00, "31-01-2023"))

#Understanding the multiple ways to format data
a = 60
b = 34.45
print("The difference of the values: {} and {} is {:.2f}.\n".format(
  a, b, a - b))

#hours to minutes conversion
hours = 2
minutes = hours * 60
print("{} hours is {} minutes\n".format(hours, minutes))

#Use of advanced python functions like math.ceil
roundedDecimal = math.ceil(a - b)
print("The rounded decimal is: {}\n".format(roundedDecimal))

#Building a calculator
print("Calculator\n-----------------------------------\n")
print(
  "1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (x)\n4. Division (÷)\n"
)

operation = int(
  input("What operation to be performed (Use the numeric index): "))

c = float(input("Enter a number: "))
d = float(input("Enter another number: "))

result = c + d if operation == 1 else (c - d if operation == 2 else
                                       (c * d if operation == 3 else c / d))
shouldRoundUp = 0
if (math.ceil(c) != c or math.ceil(d) != d):
  shouldRoundUp = 1 if input(
    "Should round up the result? (y/n): ") == "y" else 0
if shouldRoundUp == 1:
  result = math.ceil(result)
operationString =  "sum" if operation == 1 else ("difference" if operation == 2 else
                                ("product" if operation == 3 else "quotient"))
print("The {} of {} and {} is {}\n".format(
 operationString,
  c, d, result))

#Uppercase
str1 = "Hello, observe the "
str2 = "HELLO, WE ARE GOOD IN "
str3 = "ENDLESS"
print(str2.count("E", 5, 38))