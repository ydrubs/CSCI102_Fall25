##Slide 5 - Defining lists

# Three element list
# Lists can mix data types
# Lists can contain other lists
# Lists can be empty


# lists have a length
# Lists can be indexed


# Elements of sublists can be accessed from within a list



# Lists can store the result of other operation



#Slide 6 - Your turn


##Slide 7
# Iterable data types can be recast as lists





##Build a list from a string




## Other list operations
# Chek the number of elements in a list
# Combine two lists together with a '+' sign




#Slide 8
##This example allows you to add people to a roster by looping through the number of people that get added
#Get input about number
# Create an empty list to hold the people

#Loop through however many people we said we wanted to add





##This example generates n random numbers between 1 and 365 and puts them into a list




# By converting to a set data type we can see if there are any duplicates (like for the birthday problem)




##Slide 10 - Skill Review for exercise 5.1 - Stopping a loop when the 'enter' key is pressed.




#Slide 12 - Different operations and list slicing techniques that are possible
# first = [1,2,3,4]
# returns second and third element as a new list (not the fourth)
# print(first)



## Searching through a list
# find an element in a list, TRUE
# FALSE
# TRUE
# FALSE


# second = list(range(1,7))
# print(second)

## Equality vs equivalency of data:
#True because elements are not the same
#False because not the same place in memory


## Application: Searching through names in a database
import random
csci102_Roster = [
    "Jakob A. Burnett", "Ethan D. Burnum", "Jayden P. Colclasure", "Logan B. Cramer",
    "Antonio D. Flores-Ayon", "Jaden M. Grant", "Sean W. Hall", "Salvador Hernandez",
    "Caleb S. Huber", "Francisco J. Huete", "Aruchi Edmund E. Mbato", "Samantha R. Moreno",
    "Terry Nguyen", "Kayden K. Pak", "Timmy W. Reid", "Javier Ruspil",
    "Noah W. Sanchez", "Zavante Thompson", "Randy L. Towns", "Jeffrey D. Vannaman",
    "Elise R. Warden", "Jamir L. Westry", "Lexy N. Yungco"
]

# Choose a random student



##Slide 13 - Changing elements in a list
# first = [1,2,3,4]




##Slide 14 - Manipulating through looping
# numbers = [2,3,4,5]
# Looping using the index of the list



# n_lst = []
# Looping using the elements of the list to build a new list


## Loop in order to manipulate each string element
# sentence = "Python is a good beginner programming language"
# Split into individual words and make a list

#Loop through each element in the list of string by index
    #Change each word to upper case and save it into the same position



##Slide 15 - adding elements by index, without replacing data





##Slide 16 - removing elements





##Remove an element using its name by first finding its position (index)
# some_person = csci102_Roster.index("Stephen")
# print(some_person)


# To prevent an index error if the element is not found, we can write a conditional:




## Slide 18 practice exercise - IN CLASS




##Slide 20 - searching and sorting
## Building a list from conditions in another list (keep numbers greater then 15 in new list)
# from random import randint






## Slide 21
##Given a list of 20 random integers between 1 and 20, create a new list of all integers that appear more then once.






##Given TWO lists of random numbers between 1 and 20 create a new list that has the common elements of both lists
# lst2 = []
# for i in range(20):
#     lst2.append(randint(1,20))

# print(lst)
# print(lst2)


# prevents double counting the same element (unless the same element appears multiple times on both lists)




##Slide 22 - Sorting a list - NOTICE how sort() vs. sorted() behave HERE
# lst = [4,10,2,1,7]

# Using Sort()



# letters = ['c', 'h', 'b', 'A', 'M', 'B']



# Using Sorted()
# lst2 = [4,10,2,1,7]

# This returns the list sorted in numeric order
# Notice that this returns the original list - not the sorted one

# This gives us the correct sorted list



##Slide 24 - Intro to Tuples
#Empty tuple container

#Tuples of card ranks
#Tuple of tuples
#Tuple of lists


# Get element info from a tiple (similar to lists and string)


# Demonstrates you can't modify a tuple like you can a list, unless you run the line above
# If we change the cards tuple to a list we can manipulate elements


# Since the third element [2] in the first tuple is a list, it can be modified. We are not modifying the tuple itself



##SLide 26
### Application: Building a deck of cards by combining tuples
import random

# suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8','9', '10', 'jack', 'queen', 'king', 'ace')

# deck = []

        #Temporary variable to store the current card in loop
        # Show the card for debugging
        # Add this card to the deck list




##Slide 27 (IN_CLASS_TUPLE PRACTICE - point slope form)






##Slide 29
##Defining a simple function



# Need parenthesis to trigger the function



##Slide 31
##Pass arguments into a function (no limit on amount or data type)
# first name and last name are considered POSITIONAL arguments


# Pass the corresponding parameters into the function


# If you call a function that expects parameters but does not get them, you get an ERROR





##Slide 32
##Pass default values into a function (order of keyword parameters vs. positional parameters matters!)
## positional parameters need to be defines FIRST!

# These are KEYWORD Parameters


# Returns the default parameters


# Returns name as "James" instead of 'John'


# Returns a last name of "James" instead of "Doe"


# Without a parameter name they take the value based on the order (position) they are declared




## Using BOTH POSITIONAL and KEYWORD




# ERROR because POSITIONAL comes before KEYWORD



##Try it:
"""Write a function called find_bigger that accepts two decimal number and returns the bigger of the two"""





##Slide 33
"""Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise."""
# Returns True only is a string is a valid integer




# ##Slide 34
## Write a function that removes digits from a string and returns it back with only alphabetic characters.





##Slide 35
##Write a function that accepts an integer and returns the sum of its digits





###########Extra Example
"""Write a function that takes an integer and returns all integers within a range whose sum of digits is equal to the integer passed in.
For example if 11 is passed in then 29,38,47,etc.. are returned because 2+9=11, 3+8=11, etc..."""

