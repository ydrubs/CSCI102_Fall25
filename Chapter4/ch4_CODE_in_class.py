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
superhero = 'the incredible HULK'

print(superhero.upper())
print(superhero.title())
print(superhero.lower())

print(superhero.isupper()) # Is EVERY CHARACTER upper case?

another_superhero = 'spiderMan'
print(another_superhero.islower())


##Slide 12 - More Strng Methods
address = '123 Fake St.'

# Check which characters are digits
# for char in address:


# for char in address:


# for char in address:


##Slide 13 . Even more string methods
##Map a directory of files by using the split command
# string = "C:\\Users\\yuriy.drubinskiy\OneDrive - Garden City Community College\\Python Class\\Powerpoints and notes"



pass # Combining back into a single string


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
pass #True
pass # False
pass #TRUE because Ignores case-sensitivity in the string


pass # show all charaters from character 60 to character 69
pass #Since war first appears at character 67, we can see what characters 60-69 are



##Slide 16
## The variable below defines a list data structure. We will lean more about this in chapter 5
# fileList = ['myfile.txt', 'myprogram.exe', 'yourfile.txt', 'dont_open.txt']




##Slide 17 - mini task; counting letters







#Slide 21 - Writing Text to a File





## In class practice
"""
Create a text file using Python.

 Write about how cool your programming instructor is…
(or any other text you want) 

"""


#Slide 23 - Writing Numbers to a File





##Slide 24 - Reading Text from a File



## Since the text file is broken up into lines, readline() adds an extra carrige return (\n)
## This is useful if you are searching for a specific line or need to take some action based on the contents of a line
pass #As long as there's data to read, read it



##Slide 25 - Reading Numbers from a File






