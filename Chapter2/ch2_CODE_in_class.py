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
# y = x / 5
# print(x, y)# y defined in terms of x
#
#
# x = 100   # redefining x
# print(x, y)
#
#
#
# y = 2 * y   # redefining y by modifying
# print(x, y)


##Slide 15 - Review Concatenation vs. comma seperation
# first_name = "Yuriy"
# last_name = "Drubinskiy"
#
# print(first_name + ' ' + last_name, sep = '**', end = ' :) ') # Concatenation
# print(first_name, last_name, sep = '**') # comma seperated arguments


## Slide 16 - The * string operation
# s1 = 'waaz'
# s2 = 'a'
# s3 = 'p'
#
# print(s1 + s2 * 5 + s3)
# print((s1 + s2 * 5 + s3 + '\n') * 3)



### ACTIVITY slide 17 - Write a print statement that outputs the string seen in slide 17 of the powerpoint
# print ('^'*10)
# print ('#'*10)
# print ('#'*10)
# print ('#'*10)
# print ('^'*10)

# print(('^'*10 + '\n') + ('#'*10 + '\n')*3 + ('^'*10))






## Slide 20 Mixed-Mode Arithmetic
# a = 6
# b = 3
# c = 5
# d = 7.1
# print(a, type(a))
# print(a/b) # True division Results in a float
# print(a//c) # Quotient Division rounds down to an int
#
# print(a + d)



#Slide 22 - recasting review

# a = 6.1
# b = 0.1
# c = a - b # Results in a float (6.0)
# d = c +1
# print(d) # Still a float
# print(int(d))
#
# d = str(d)
# print(d, type(d)) # See 7.0 (but as string)
#
#
# print(float('7.5'))

## SLide 23 rounding floats
# a = 3.14159
#
# print(round(a, 0))
# print(round(a, 1))
# print(round(a, 2))

# b = 1.2345
# print(f"{a:.2f}")



##Slide 24 - Character operations
s1 = "Mary"
s2 = "Freddy"

pass #Get the lenght of string s1 and s2
print(ord('A')) # Get the ASCII code of the character
print(chr(65)) #Get the character from the ASCII code
print(chr(ord("A")+1))
pass #Find the smallest and largest ASCII character of s2


##Playing around with some character codes in unicode
# print(chr(0x265e))
# print(chr(0x250C))
# print(chr(203850))
# print(int(0x265e))
# print(chr(9822))

# print('The ASCII code for the letter \'a\' is ' + str(ord('a')))

# for i in range (9000, 100000):
#     print(chr((i)), end = ', ')

print(int("hello"))