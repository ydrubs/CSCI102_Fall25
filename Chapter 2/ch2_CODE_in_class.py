"""
This is example code for Chapter 2
This is code we did in class
"""

# ##Slide 2
age = 122 # age of the oldest ever living person
# # give the age of the person
# print(age)

"""Sometimes there is a need to explain or document a portrion of code beyond one line.
For this we can use a docstring to extend to multiple lines.
Docstrings are also used to attribute programs and explain functions."""

# a = '2'
# b = 2
# print(a,b)
# print(type(b))

##Slide 5
# print(1,234)
# print(1_234)




##Slide 7
# print("that's")
#
# print("A double quoted string")
# print('does the same thing as a single quoted string')

# print("However, there'll be times when a string needs to include a single quote within it, so a double quote is useful.")

#Printing Multiline strings
# welcomeText = '''Welcome to my game!
# I will think of a number from 1 to 100, and you must try
# to guess it. I'll tell you if your guess is too small
# or too large.
#
# Enter an integer between 1 and 100 when prompted.'''
#
# print(welcomeText)


##Slide 8
# print('Hello. \nHow \nare \nyou?')
#
# print("1. hello " + 'there') #Substitute one of the escape chars for the '#'
# print("2. hello\b " + ' there')
# print("3. hello\n " + ' there')
# print("4. hello\t " + ' there')
# print("5. hello\\ " + ' there')
# print("6. hello\' " + ' there')
# print("7.hello\" " + ' there')


###Activity - slide 9 Experiment with escape character in the space below
# s1 = "Green eggs and ham"
# s2 = 'Sam-I-am'
# s3 = "I do not like them\n Sam-I-am!"
# print(s3)



##Slide 10
# print("Hello")
# print("there")
#
# print("Hello", end=' ')
# print('there')
#
# print("Hello", end=' :) :) ')
# print('there')


##Slide 11
# name = 'Yoda'
# age = 900
# home_planet = 'Dagobah'
# #
# print(name,age,home_planet)
# print(name,age,home_planet, sep = '\n')
# print(name,age,home_planet, sep = '**', end = ' :) ')
# print("The End")

###Activity from slide 13
#Three 'Good' Variables
# HITHERE = 'Hello'
# hiThere = 'Hello'
# hi_th0re = 'Hello'

#Three Invalid variables
# 1hi_there = 'hello'
# if = 'hello'
# hi! = 'Hello'

##Slide 14
# first_name = "Obi-Wan"
# last_name = "Kenobi"
# full_name = first_name + last_name
# print(full_name)

### Skill Check
# print('Hello')
# print("World")
#
# print("Hello", end = '\n')
# print("WOrld")

# print("Hello" + "World", sep = '....')
# print("Hello", "World", sep = '....')

# a = 2
# print(f'The number is {a}') #F-string



# #Reassigning Variables to new values
# x = 125
# y = x / 5    # y defined in terms of x
# print(x, y)
# # #
# x = 100    # redefining x
# print(x, y)
# # #
# y = 2 * y    # redefining y by modifying
# print(x, y)

##Slide 15
# first_name = "Yuriy"
# last_name = "Drubinskiy"
#
# print(pass)
# print(pass)


# s1 = 'waaz'
# s2 = 'a'
# s3 = 'p'
# print(s1 + s2*5 + s3)
# print((s1 + s2*5 + s3 + ' ')*3)


###ACTIVITY slide 16
# print(('^' * 10 + '\n') + (('#' * 10 + '\n')*3) + ('^' * 10 + '\n'))


##Slide 18 - Examples of right associative
# print(9**0.5) #Exponents
# print(10//9) # QUOTIENT
# print(9%2)
# print(13%5)

# print(2**3**4)
# print(2**81)
#
# a = 1
# a = a + 1
# print(a)



## Slide 20
# a = 6
# b = 3
# print(a, type(a))
# print(a/b, type(a/b))
# print(a//b, type(a//b))
#
# c = 0.7
# print(a+c, type(a+c))


#Slide 21
# a = 6.1
# b = a-0.1
# print(b+1, type(b+1))

#Slide 23
# d = 3.14
# print(3/d)


# print(round(6.75,0))
# print(round(6.75,1))
# print(round(6.75,2))
# print(round(6.75,3))

# print('$' + 100) # No good
# print('$' + str(100)) #This is okay
# print(f'$ {100}') # This is okay too
# print('$', 100, sep = '') # This is okay too

##Slide 24
s1 = "Mary"
s2 = "Freddy"

# print(len(s1)) #Get the lenght of string s1 and s2
# print(ord('M'), ord(s1[0])) # Get the ASCII code of the character
# print(chr(99+1)) #Get the character from the ASCII code
# print(min(s2), max(s2)) #Find the smallest and largest ASCII character of s2


##Playing around with some character codes in unicode
# print(chr(0x265e))
# print(chr(0x250C))
# print(chr(203850))
# print(int(0x265e))
# print(chr(9822))

# print('The ASCII code for the letter \'a\' is ' + str(ord('a')))

# for i in range (9000, 10000):
#     print(chr((i)), end = ', ')

print(chr(ord('a')+10))
