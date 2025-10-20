# #Slide 3 - String from characters demo
# string = 'Hello to you'
#
#
# for char in string: #Iterate through the individual characters
#     print(char)

# n = 32
# for digit in n:## This will give an ERROR because an integer is not ITERABLE
#     print(digit)




#Slide 4 - exploring string indexes
# name = 'Skywalker'
# print(name[0]) #The first letter is 'S'
# print(len(name))

# print(name[9]) #Results in an index error because last index is at [8]
# print(name[len(name)-1]) # This ensures you will print the last letter

# print(name[-1]) # last character is 'r'
# print(name[-2]) #  Second to last character is 'e'
# print(name[-1*len(name)]) # This also gives last letter



##Slide 5
# data = 'Hi there!'
# print(data[len(data)])

## Loop Through the indexes of the string (these are numbers)
# for i in range(len(data)):
#     print(i, data[i])


## Loop through the elements of the string
# for char in data:
#     print(char)


### YOUR TURN
# song = 'Harmony Hall'
#
# print(song[1])
# print(len(song))
#
# for i in range(len(song)):
#     print(song[i], end = ':)')
#
# for char in song:
#     print(char)



##Slide 7 - Mutable vs. Immutable Data
# mutable = ['G', 'O', 'O', 'D']
# print(mutable[0])
# mutable[0] = 'H' # Reassigning 'G' to an 'H'
# print(mutable) # print entire list


# immutable = 'Good'
# print(immutable[0])
# immutable[0] = 'H' # This will give an error because a string is IMMUTABLE, since you can't change a single element

# immutable = 'Hood' # Reassigning variable to something else is OKAY
# print(immutable)



##Slide 9 - string slicing
name = 'myfile.txt'
# print(name[0:]) # full string

# print(name[0:1]) # Only the first character

# print(name[0:2]) # First two characters

# print(name[2:6]) # Start at the third character stop at the 6'th character

# print(name[:2]) # This is the same as name[0:2]

# print(name[-3:-1]) # Start at third to last and go to last

# print(name[0::2]) # Start at the beginning and go every other letter

# print(name[-1::-1]) # Full string Backwards

# print(name[::2]) # Every other character of full string


# print(name[100]) #ERROR
# print(name[0:100]) # This is okay

# print(name[0:3] + name[3:])

##Slide 9 - Try to run your own experiments with the string below
# my_string = "Give a man a program, frustrate him for a day. " \
#             "Teach a man to program, frustrate him for a lifetime."
#
# print(my_string[10:20])

##Slide 10 - Your turn - Move Two Letters
# my_string = input("Please enter a string to rearrange: ")
#
# print(my_string[-2:] + my_string[:-2])



##Slide 11 - String Methods
# superhero = 'the incredible HULK'
#
# print(superhero.upper())
# print(superhero.title())
# print(superhero.lower())
#
# print(superhero.isupper()) # Is EVERY CHARACTER upper case?
#
# another_superhero = 'spiderMan'
# print(another_superhero.islower())


##Slide 12 - More String Methods
address = '123 Fake St.'

# Check which characters are digits
# for char in address:
#     print(char, char.isdigit())
#
# for char in address:
#     print(char, char.isupper())

# for char in address:
#     print(char, char.isspace())
#

##Slide 13 . Even more string methods
##Map a directory of files by using the split command
# string = "C:\\Users\\yuriy.drubinskiy\\OneDrive - Garden City Community College\\Python Class\\Powerpoints and notes"
# print(string)

# string = string.split('\\')
# print(string)


# string = '*'.join(string) # Combining back into a single string
# print(string)


##Slide 13/14 - STRING METHODS SUMMARY
####Commands that let you access and see info about what string methods do
# greeting = 'hello'
# print(dir(greeting)) # A list of available methods for the 'string' object
# print(help(str)) # A more detailed description of each available method



##Slide 15 - Testing string logic with 'in'
# text = """A long time ago in a galaxy far far away..
# It is a period of civil war.
# Rebel spaceships, striking
# from a hidden base, have won
# their first victory against
# the evil Galactic Empire."""
#
# print('time' in text) #True
# print('empire' in text) # False
# print('empire' in text.casefold()) #TRUE because Ignores case-sensitivity in the string
#
#
# print(text.index('war')) # show all charaters from character 60 to character 69
# print(text[60:70]) #Since war first appears at character 67, we can see what characters 60-69 are




##Slide 17 - mini task; counting letters
# import this
# words_of_wisdom = """The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""
#
# count = 0
# FInd the number of 'e' and 'a' in the text
# for letter in words_of_wisdom:
#     print(letter)
#     if letter == 'e':
#         count +=1
#     elif letter == 'a':
#         count +=1

# print(count)

# Boolean Flag demo
# Checks for an "A" or a number before breaking loop
# while True:
#     my_string = input("Please enter a string: ")
#
#     # Set flags (assume both conditions are false)
#     has_A = False
#     has_number = False
#
#     # CHeck each character in the input
#     for char in my_string:
#         if char == "A":
#             print("Found an A!")
#             has_A = True
#         elif char.isdigit():
#             print("Found a number!")
#             has_number = True
#
#     if has_A and has_number:
#         print("String is valid")
#         break
#     else:
#         print("String is not valid")


# some_string = ""

#Slide 22 - Writing Text to a File
# f = open('myfile.txt', 'w')
# f.write("1. Venus - 5,832 hours\n"
#         "2. Mercury - 1,408 hours\n"
#         "3. Mars - 24.6 hours\n"
#         "4. Earth - 24 hours")
# f.close()



## In class practice
"""
Create a text file using Python.

 Write about how cool your programming instructor is…
(or any other text you want) 

"""



#Slide 24 - Writing Numbers to a File
# from random import randint
# f = open('integers.txt', 'w')
#
# for count in range(500):
#         number = randint(1,500)
#         f.write(str(number) + '\n')
#
# f.close()




##Slide 25/26 - Reading Text from a File
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)



## Readline() returns the file line by line
## This is useful if you are searching for a specific line or need to take some action based on the contents of a line

# f = open('myfile.txt', 'r')
# while True: #As long as there's data to read, read it
#         line = f.readline()
#         if line == "":
#                 break
#         print('Data Processed' + line)


##Slide 27 - Reading Numbers from a File
f = open('integers.txt', 'r')

theSum = 0
for line in f:
        number = int(line)
        theSum += number
print(f"The sum is {theSum}")




