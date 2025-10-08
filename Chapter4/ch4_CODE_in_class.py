# #Slide 3 - String from characters demo


pass #Iterate through the individual characters


## This will give an ERROR because an integer is not ITERABLE




#Slide 4 - exploring string indexes
name = 'Skywalker'
pass #The first letter is 'S'


pass #Results in an index error because last index is at [8]
pass # Also an error because len(name) looks at index 9 as well


pass # last character is 'r'
pass #  Second to last character is 'e'



##Slide 5
data = 'Hi there!'

## Loop Through the indexes of the string (these are numbers)




## Loop through the elements of the string




### YOUR TURN





##Slide 7 - Mutable vs. Immutable Data
# mutable = ['G', 'O', 'O', 'D']



# immutable = 'Good'





##Slide 9 - string slicing
name = 'myfile.txt'
pass # full string
pass # Only the first character
pass # First two characters
pass # Character 2 to 5
pass # This is the same as name[0:2]

pass # Start at third to last and go to last
pass # Start at the beginning and go every other letter


pass #ERROR
pass # This is okay
pass # Last three characters combined with the character 2 to 5


##Slide 9 - Try to run your own experiments with the string below
# my_string = "Give a man a program, frustrate him for a day. " \
#             "Teach a man to program, frustrate him for a lifetime."



##Slide 10 - Your turn - Move Two Letters




##Slide 11 - String Methods
superhero = 'incredible HULK'




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






