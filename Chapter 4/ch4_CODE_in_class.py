# #Slide 3
# string = 'Hello to you'
# for char in string: #Iterate through the individual characters
#     print(char)

#This will give an ERROR because an integer is not ITERABLE
# n = 10
# for digit in n:
#     print(digit)

# The Length of a string (IMPORTANT TO KNOW)
# print(len(string))
# print(len(".,jsnf;ksdnc;ksdnc;isnc;kjdsnfek .kdsnfj"))

# print()
# print(string[4]) #print the character at the specified index


#Slide 4
name = 'Skywalker'
# print(name[0]) #The first letter is 'S'
# print(len(name))
#
# print(name[9]) #Results in an index error
# print(name[len(name)]) # Also an error because len(name) is 9


# print(name[-1]) # last character is 'r'
# print(name[-2]) #  Second to last character is 'e'

##Slide 5
data = 'Hi there!'
#
# ###Loop Through the indexes of the string (Important)
# for char in range(len(data)):
    # print(char) # only counts numbers this way
    # print(data[5])
#
# ##Loop through the elements of the string
# for char in data:
#     print(char)


### YOUR TURN
# song = 'Harmony Hall'
# print(song[1])
# print(len(song))
#
# for i in range(len(song)):
#     print(song[i], end = ':)')
#
# for char in song:
#     print(char)

##Slide 7
# mutable = ['G', 'O', 'O', 'D']
# print(mutable[0])
# mutable[0] = 'H'
# print(mutable)

# immutable = 'Good'
# print(immutable)
# print(immutable[0]) #This command is fine
#
# # immutable[0] = 'H' # ..This is not. Can't override the individuals characters
# immutable = 'Hood' #...But you can override the variable itself
# print(immutable)

##Slide 9
name = 'myfile.txt'
# print(name[0:])
# print(name[0:1])
# print(name[0:2])
# print(name[2:6])
# print(name[:2]) # THis is the same as name[0:2]

# print(name[-3:-1]) # Start at third to last and go to last
# print(name[0::2]) # Start at the beginning and go every other letter
#

# print(name[100]) #ERROR
# print(name[0:100])# This is okay
# print(name[-3:-1] +  name[2:6])


##Slide 9 - Try to run your own experiments with the string below
# my_string = "Give a man a program, frustrate him for a day. " \
#             "Teach a man to program, frustrate him for a lifetime."

##Slide 10 - Your turn - Move Two Letters
# a = input("Enter a string, please: ")
# print(a[-2:] + a[0:-2])


##Slide 11
superhero = 'incredible HULK'

# print(superhero.upper())
# print(superhero.title())
# print(superhero.lower())
# print(superhero.isdigit())


##Slide 12
address = '123 Fake St.'

# Check which characters are digits
# for char in address:
#     print(char.isdigit())
#
# for char in address:
#     print(char.isupper())
#
# for char in address:
#     print(char.isspace())


##Slide 13
##Map a directory of files by using the split command
# string = "C:\\Users\\yuriy.drubinskiy\OneDrive - Garden City Community College\\Python Class\\Powerpoints and notes"
# string = string.split('\\')

# print(string)

# print('*'.join(string)) # Combining back into a single string


##Slide 13/14 - STRING METHODS SUMMARY
####COmmands that let you access and see info about what string methods do
# greeting = 'hello'
# print(dir(greeting)) # A list of available methods for the 'string' object
# print(help(str)) # A more detailed description of each available method


##Slide 15
# text = """A long time ago in a galaxy far far away..
# It is a period of civil war.
# Rebel spaceships, striking
# from a hidden base, have won
# their first victory against
# the evil Galactic Empire."""
#
# print('time' in text) #True
# print('empire' in text) # False
# print('galactic' in text.casefold()) #TRUE because Ignores case-sensitivity in the string

#
# print(text[60:70]) # show all charaters from character 60 to character 69
# print(text.index('war')) #SInce war first appears at character 67, we can see what characters 60-69 are



##Slide16
##he variable below defines a list data structure. We will lean more about this in chapter 5
# fileList = ['myfile.txt', 'myprogram.exe', 'yourfile.txt', 'dont_open.txt']
# for file in fileList:
#     if '.txt' in file:
#         print(file)

##Slide 17
# import this
# words_of_wisdom = """
# The Zen of Python, by Tim Peters
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
# print(words_of_wisdom)
# words = words_of_wisdom.split('a')
# print(words)
#
# count = 0
# for word in words:
#     if 'a' in word or 'e' in word:
#         count +=1
# print(count)
#
# print(words_of_wisdom.count('e') + words_of_wisdom.count('a'))


#Slide 21
f = open('myfile.txt', 'w')
f.write("1. Justin Herbert $52.5 million\n2. Lamar Jackson $52 million\n3.Jalen Hurts $51 million\n\n This is not valid anymore")
f.close()

## In class practice
"""
Create a text file using Python.

 Write about how cool your programming instructor is…
(or any other text you want) 

"""


#Slide 23
# import random
# f = open('integers.txt', 'w')
#
# for count in range(500):
#     number = random.randint(1,100)
#     f.write(str(number) + '\n')
#
# f.close()


##Slide 24
# f = open("myfile.txt", 'r')
# text = f.read()
# print(text)

# #
# # ##Since the text file is broken up into lines, readline() adds an extra carrige return (\n)
# while True: #As long as there's data to read, read it
#     line = f.readline()
#     if line == '':
#          break
#
#     print(line)


##Slide 25
# f = open('integers.txt', 'r')
# theSum = 0
#
# for line in f:
#     number = int(line)
#     theSum += number
#
# print('The sum is', theSum)


""""
We didn't cover this in class.
It discusses splitting data that is not being read line-by-line rather seperated by a space character.
This isn't crucial at this point in the class so we won't get bogged down with the details.
"""
##Slide26
###GENERATE SOME DATA TO BE READ
import random

f = open('integers2.txt', 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + ' ') # Create random ints with a space seperator
f.close()

# ###Read from the file and sum it
f = open('integers2.txt', 'r')
theSum = 0
for line in f:
    wordlist = line.split() #Split on space or newline (you can specify a string argument for other seperators)
    for word in wordlist:
        number = int(word)
        theSum += number
print('The sum is', theSum)
