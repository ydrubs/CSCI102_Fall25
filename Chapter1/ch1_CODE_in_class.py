### Slide 5 - Simple Hello World Program
#print("Hello world")
#greet = "How is your day"
#print(greet)

# print(id(greet))

###Slide 15 - Data types
# hello = 'hello'
# print(type(hello))
# #
# number = 150
# print(type(number))
# #
# a_bool = True
# print(type(a_bool))
# #
# hello = number
# print(type(hello))
#
# score = 3.14
# print(type(score))

###Slide 17 - Getting Input

## All inputs in Python are strings by default
# name = input("Enter your name please: ")
# age = input("Enter your age: ") # Age is a string
#
# print(name)
# print(age)
# print(type(age))
#
#
# print(age + 1) # This is an error because its trying to combine a string with a none-string

##Slide 18 Activity
# print("Welcome to class")
#
# name = input("Enter your name: ")
# print("Welcome " + name + " to class.")




####Slide 19 Recasting Input
# a = input("Enter the first number: ") # THis gives a string
# b = input("Enter the second number: ") # This gives a string
#
# print(a+b)

# c = int(input("Enter the first number: ")) # THis is not an integer
# d = int(input("Enter the second number: "))
#
# print(c + d)

# f = float(input("Enter the first number: ")) # THis is now a float
# g = int(input("Enter the second number: "))
#
# print(f + g)



###Slide 22 Outputting multiple data
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))


# print('Hello',name,'you are',age,'years old.') # Using commas to seperate data
# print('Hello ' + name,' you are ' + str(age),'years old.') # Using + to concatenate data into one string

# print(f"Hello, {name}, you are {age + 1} years old") # Using f-strings



###Slide 23 Operations
a = int(input("first number: ")) # Suppose 7
b = int(input("Second number: ")) # Suppose 4


# print(a + b) # you'll get 11
# print(a - b) # 3
# print(a * b) # 28
#
# print(a/b) # Regular division, always a FLOAT
# print(a//b) # Quotient division, always an integer rounded down

print(a % b)# Modulus

##Slide 28
##Run-Time error - Program stops execution when it encounters an error
# length = int(input("Enter the length: "))
# print(legnth) # Stops execution HERE


##Syntax Error - Program does not execute at all
# length = int(input("Enter the length: "))
# print{legnth} # SYNTAX ERROR Here


##Sementic Error
# length = int(input("Enter the length: "))
# print("The area of the square is ", 2*length)


##Slide 29
 # print("Hello")


# a = 2
# b = 3
# print(a +)


##Slide 30
##Traceback
# def say(name):
#     print('Hello, ' + nam)
#
# say('Michael')
