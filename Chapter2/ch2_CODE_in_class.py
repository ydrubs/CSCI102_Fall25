"""
This is example code for Chapter 2
This is code we did in class
"""

##Slide 2 - Example of comments and docstrings
age = 115 # age of the oldest ever living person
# # give the age of the person
# print(age)

"""
Sometimes there is a need to explain or document a portrion of code beyond one line.
For this we can use a docstring to extend to multiple lines.
Docstrings are also used to attribute programs and explain functions.
"""

##Slide 5 - place value representation
# a = 423_192_374_983_274
# print(a, type(a))




##Slide 7 - String literals
# print("hello there")
# print('hello there') # Both are the same

# print('That's awesome) #Gives an error because an apostr. is part of the string
# print("That's awesome") # This fixes the problem, woohoo
# print('That\'s awesome') # This also fixes it


##Slide 8 - Escape characters
# print('Hello. \n\tHow \n\t\tare \n\t\t\tyou?')
#
# print("1. hello " + 'there') #Substitute one of the escape chars for the '#'
# print("2. hello\b " + ' there')
# print("3. hello\n " + ' there') #\n this is the one most used
# print("4. hello\t " + ' there')
# print("5. hello\\ " + ' there')
# print("6. hello\' " + ' there')
# print("7.hello\" " + ' there')




##Slide 10 - End of line arguments
# import time
# print("Hello", end = "**")
# time.sleep(1)
# print("there")
# time.sleep(1)
# print('How')
# time.sleep(1)
# print('are')
# time.sleep(1)
# print('you')


##Slide 11 - separator arguments
# name = 'Yoda'
# age = 900
# home_planet = 'Dagobah'

## using sep
# print(name, age, home_planet)
# print(name, age, home_planet, sep = '\n')

# print(name + str(age) + home_planet, 'woot', sep = '**')

##  combine sep and end
# print(name, age, home_planet, sep = '**', end = ' tacos ')
# print("The end")

###Activity from slide 13
## Five valid Variables
# HITHERE = 'hello'
# hithere = 'hello'
# hi_there = 'hello' # this one is good convention
# _hi_there = 'hello'
# hi123 = 'hello'

## Three Invalid variables
# 1hi_there = 'hello' # can't START with a number, boo
# if = 'then' #Can't use reserved words
# hi! = 'hello' # can't use special character (including space)

## ACTIVITY


##Slide 14 - variable assignment through concatenation
# first_name = "Obi-Wan"
# last_name = "Kenobi"




## Reassigning Variables to new values
x = 125
y = x / 5
print(x, y)# y defined in terms of x


x = 100   # redefining x
print(x, y)



y = 2 * y   # redefining y by modifying
print(x, y)


##Slide 15 - Review Concatenation vs. comma seperation
# first_name = "Yuriy"
# last_name = "Drubinskiy"

pass # Concatenation
pass # comma seperated arguments


## Slide 16 - The * string operation
s1 = 'waaz'
s2 = 'a'
s3 = 'p'





### ACTIVITY slide 17 - Write a print statement that outputs the string seen in slide 17 of the powerpoint



##Slide 18 - Examples of math operations
pass #Exponents
pass # QUOTIENT
pass # Modulus (mod)
pass

pass
pass



# a = 1
pass # Increment and reassign to itself




## Slide 20 Mixed-Mode Arithmetic
# a = 6
# b = 3
pass
pass # True division Results in a float
pass # Quotient Division rounds down to an int


# c = 0.7
pass # Addition using at least one float always results in a float





#Slide 22 - recasting review
a = '33'
b = 5
c = 4.0
d = 'one'

pass # int to float
pass # float to str
pass # str to int
pass # str to int - ERROR


## SLide 23 rounding floats





##Slide 24 - Character operations
# s1 = "Mary"
# s2 = "Freddy"

pass #Get the lenght of string s1 and s2
pass # Get the ASCII code of the character
pass #Get the character from the ASCII code
pass #Find the smallest and largest ASCII character of s2


##Playing around with some character codes in unicode
# print(chr(0x265e))
# print(chr(0x250C))
# print(chr(203850))
# print(int(0x265e))
# print(chr(9822))

# print('The ASCII code for the letter \'a\' is ' + str(ord('a')))

# for i in range (9000, 10000):
#     print(chr((i)), end = ', ')

