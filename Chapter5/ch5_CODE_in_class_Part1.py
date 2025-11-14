##Slide 5 - Defining lists


fruits = ['apples', 'oranges', 'bananas'] # Three element list
ultra_fruit = fruits[0] + fruits [1]
# print(ultra_fruit)

lst = [24, 3.2, 'hello', True] # Lists can mix data types
coordinates = [[-3,1], [0,3]] # Lists can contain other lists
freinds = [] # Lists can be empty

# print(len(fruits))# lists have a length
# print(fruits[1])# Lists can be indexed
# print(lst[-1]) # Index from the back

# print(coordinates[0]) # Elements of sublists can be accessed from within a list
# print(coordinates[1][0]) # Access a sublist element

# print(lst[4]) # Error because no element at index 4

# Lists can store the result of other operation
# import math
# x = 4
# math_stuff = [x, math.sqrt(x), math.pi, x + 1]
# print(math_stuff[1]) # gives you 2
# print(math_stuff[x-1]) # gives you __________


#Slide 6 - Your turn


##Slide 7
# Iterable data types can be recast as lists
from random import randint, choice
first = [1,2,3,4]
# second = list(range(1,53))
# print(second)
# print(first[1] + first[3])
# print(type(first[1])) # second element is an int
# print(type(first))
# print(first + second)

# print(max(first))
# print(min(second))
# print(sum(second))

# print(second[randint(1,53)])
# print(choice(second))

##Build a list from a string
message = "a Z"
message_lst = list(message)
# print(message_lst)
#
# print(max(message_lst))

## Other list operations
# print(len(message_lst)) # Chek the number of elements in a list
# print(message_lst + first)# Combine two lists together with a '+' sign




#Slide 8
##This example allows you to add people to a roster by looping through the number of people that get added
# roster_size = int(input("How many people do you want to add: ")) #Get input about number
# roster = [] #  Create an empty list to hold the people
#
# for i in range(roster_size): #Loop through however many people we said we wanted to add
#     new_member = input("Enter the members name: ")
#     roster.append(new_member)
#
# print(roster)




##This example generates n random numbers between 1 and 365 and puts them into a list
# from random import randint
# number_lst = []
# n = 60
#
# for i in range(n):
#     number = randint(1,365)
#     number_lst.append(number)
#
# print(number_lst)
#

# By converting to a set data type we can see if there are any duplicates (like for the birthday problem)
# no_duplicates = set(number_lst)
# print(len(number_lst), len(no_duplicates))


##Slide 10 - Skill Review for exercise 5.1 - Stopping a loop when the 'enter' key is pressed.
# while True:
#     data = input("Enter SOMETHING!!!!: ")
#     if data == '':
#         break



#Slide 12 - Different operations and list slicing techniques that are possible
first = [1,2,3,4,5,6]
# first = first[2:4] # returns second and third element as a new list (not the fourth)
# print(first)
# second = first[::]
# print(second)


# second = first

# new_list = []
# for element in first:
#     print(element)
#     str_numb = float(element)
#     new_list.append(str_numb)
# print(new_list)


## Searching through a list
# print(1 in first) # find an element in a list, TRUE
# print('1' in first)# FALSE
# print(int('1') in first)# TRUE
# print(str(1) in first)# FALSE


# second = list(range(1,7))
# print(second)

## Equality vs equivalency of data:
# print(first == second) #True because elements are not the same
# print(first is second) #False because not the same place in memory


# first[1] = 'hello'
# print(first)
# first[-1] = 3.14
# print(first)

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

# random_student = random.choice(csci102_Roster) # Choose a random student
# print(random_student)
# print('Bob' in csci102_Roster) # False
#
# print('Jamir L. Westry' in csci102_Roster)
#
# print(f"{random.randint(-10,10)} points of extra credit goes to {random_student}")


##Slide 13 - Changing elements in a list
# first = [1,2,3,4]

# csci102_Roster[1] = 'Taylor Swift'
# print(csci102_Roster)
#


##Slide 14 - Manipulating through looping
# numbers = [2,3,4,5,6, 7]
# Looping using the index of the list
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] ** 2
# print(numbers)


# n_lst = []
# for number in numbers: # Looping using the elements of the list to build a new list
#     n_lst.append(number)
# print(n_lst)
# n_lst.append(64)
# print(n_lst, numbers)

## Loop in order to manipulate each string element
# sentence = "Python is a good beginner programming language"
# sentence_lst = sentence.split()# Split into individual words and make a list
# print(sentence_lst)
# print(len(sentence), len(sentence_lst))
#
# for i in range(len(sentence_lst)):#Loop through each element in the list of string by index
#     sentence_lst[i] = sentence_lst[i].upper() #Change each word to upper case and save it into the same position
#     print(sentence_lst[i])
#
# print(sentence_lst)


##Slide 15 - adding elements by index, without replacing data
# csci102_Roster.insert(1, "Spongebob")
# print(csci102_Roster)

# csci102_Roster.insert(-1, "10")
# print(csci102_Roster)

# csci102_Roster.append('Michael Jordan')
# print(csci102_Roster)

# new_students = ['Larry', 'Curly', 'Moe']
# csci102_Roster.extend(new_students)
# print(csci102_Roster)

# big_roster = csci102_Roster + new_students # Does the same thing as extend
# print(csci102_Roster)
# print(big_roster)


##Slide 16 - removing elements
# last_person = csci102_Roster[-1]
# print(last_person)
#
# last_person = csci102_Roster.pop()
# print(csci102_Roster)
# print(last_person)
#
# first_person = csci102_Roster.pop(0)
# print(csci102_Roster)
# print(first_person)



##Remove an element using its name by first finding its position (index)
# some_person = csci102_Roster.index("Antonio D. Flores-Ayon")
# print(some_person)
#
# some_person = csci102_Roster.pop(some_person)
# print(some_person)


# To prevent an index error if the element is not found, we can write a conditional:
# csci102_Roster.append(some_person)
# name = some_person
# if name in csci102_Roster:
#     person = csci102_Roster.index(name)
#     print(f"Hi {name}!!!!")
# else:
#     print(f'{name} is not in the Roster')


## Slide 18 practice exercise - IN CLASS
## Generate a list of 10 random elements that are either 0 or 1, then replace all the 1's with the string 'valid'
# from random import randint
# lst = []
#
# for i in range(10):
#     lst.append(randint(0,1))
# print(lst)
#
# modified_list = []
# for i in range(len(lst)):
#     print(lst[i])
#     if lst[i] == 1:
#         modified_list.append('valid')
#     else:
#         modified_list.append(lst[i])
# print(modified_list)





##Slide 20 - searching and sorting
## Building a list from conditions in another list (keep numbers greater then 15 in new list)
# from random import randint
# from random import randint
# lst = []
#
# for i in range(20):
#     lst.append(randint(1,20))
# print(lst)
#
# new_lst = []
# for number in lst:
#     if number > 15:
#         new_lst.append(number)
#
# print(new_lst)





## Slide 21
## Given a list of 20 random integers between 1 and 20, create a new list of all integers that appear more then once.
# from random import randint
# lst = []
#
# for i in range(20):
#     lst.append(randint(1,20))
# print(lst)
#
# new_lst =[]
# # print(lst.count(3))
#
# for number in lst:
#     if lst.count(number) > 1:
#         if number not in new_lst:
#             new_lst.append(number)
#
# print(new_lst)




##Given TWO lists of random numbers between 1 and 20 create a new list that has the common elements of both lists
# from random import randint
# lst = []
#
# for i in range(20):
#     lst.append(randint(1,20))
#
# lst2 = []
# for i in range(20):
#     lst2.append(randint(1,20))
#
# print(lst)
# print(lst2)
#
# new_lst = []
# for number in lst:
#     if number in lst2:
#         new_lst.append(number)
#         lst2.pop(lst2.index(number))# prevents double counting the same element (unless the same element appears multiple times on both lists)
#
# print(new_lst)
#


##Slide 22 - Sorting a list - NOTICE how sort() vs. sorted() behave HERE
# lst = [4,10,2,1,7]

# Using Sort()
# lst.sort() # sort in-place
# print(lst)
# lst.sort(reverse = True)
# print(lst)


# letters = ['c', 'h', 'b', 'A', 'M', 'B', 'a']
# letters.sort()
# print(letters)


# Using Sorted()
# lst2 = [4,10,2,1,7]


# new_lst = sorted(lst2)# This returns the list sorted in numeric order
# print(lst2)# Notice that this returns the original list - not the sorted one

# This gives us the correct sorted list
# print(new_lst)


##Slide 24 - Intro to Tuples
# cards = () #Empty tuple container
# print(type(cards))
#
# cards = (6,7,8,9,10, 'Jack') #Tuples of card ranks
# cards_full = ((2, 'hearts'), (8, 'spades')) #Tuple of tuples
# print(cards_full[0]) # prints (2, 'hearts')
# print(cards_full[0][1]) # print 'hearts' from the first tuple in cards_full
#
# cars =([2020, 'Chevy', 'Corvette'], [2023, 'Toyota', 'Prius']) #Tuple of lists
# print(cars[0])
# # cars[0] = [2020, 'Ford', 'A'] # Cant change a tuple element
# cars[0][0] = 2021 # This is fine - changes the first element of the first list
# print(cars)
#
#
# cards_lst = list(cards) # If we change the cards tuple to a list we can manipulate elements
# print(cards_lst)
# cards_lst[0] = 'Ace'
# print(cards_lst)
#

##SLide 26
### Application: Building a deck of cards by combining tuples
import random

# suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8','9', '10', 'jack', 'queen', 'king', 'ace')
#
# deck = []
# for suit in suit_tuple:
#     for rank in rank_tuple:
#         card = (rank, suit) #Temporary variable to store the current card in loop
#         # print (card) # Show the card for debugging
#         deck.append(card)# Add this card to the deck list
#
# print(deck)
# print(len(deck))
#
# random.shuffle(deck)
# print(deck)
# print(random.choice(deck))


## Slide 27 (IN_CLASS_TUPLE PRACTICE - point slope form)
# point1 = (2,6)
# point2 = (-3, 8)
#
#
# x1 = point1[0]
# x2 = point2[0]
# y1 = point1[1]
# y2 = point2[1]
#
# slope = (y2 - y1) / (x2 - x1)
# print(f"The slope is {slope}")




##Slide 29
##Defining a simple function
# def greeting():
#     print("I am a function")
#     return 'Hi Everyone'
    # print("Goodbye") # This won't run after the return

# greeting() # Need parenthesis to trigger the function
# print(greeting()) # Shows what the function returns
# hello = greeting() # Stores the output of a function to a variable
# print(hello) # THe return statement is stored in 'hello' variable
#
# print(greeting) # Shows where function lives in memory


##Slide 31
##Pass arguments into a function (no limit on amount or data type)
# first name and last name are considered POSITIONAL arguments
# def greeting(first_name, last_name):
#     data = f'Call me {last_name}, {first_name}, {last_name}'
#     return data

# greet_me = greeting("James", "Bond")# Pass the corresponding parameters into the function
# print(greet_me)


# greet_me = greeting()# If you call a function that expects parameters but does not get them, you get an ERROR





##Slide 32
##Pass default values into a function (order of keyword parameters vs. positional parameters matters!)
## positional parameters need to be defines FIRST!
# def greeting(first_name = "James", last_name = "Bond"):
#     data = f'Call me {last_name}, {first_name}, {last_name}'
#     return data
#
# greet_me = greeting()# These are KEYWORD Parameters
# print(greet_me) # Prints default parameters
#
# greet_me = greeting(last_name = "Spongebob", first_name = 'Squidward')
# print(greet_me)



## Using BOTH POSITIONAL and KEYWORD
# def greeting(first_name : str, last_name = "Bond"):
#     data = f'Call me {last_name}, {first_name}, {last_name}'
#     return data
#
# # greet_me = greeting() # Will give an error, 1 argument
# greet_me = greeting("James") # This is fine because last name has a default value
# greet_me = greeting("James", last_name = 'Lebron') # THis is fine too
# print(greet_me)


# ERROR because POSITIONAL comes before KEYWORD
# def greeting(first_name = "James", last_name): # Keyword argument is first, positional is second - BIG NO
#     data = f'Call me {last_name}, {first_name}, {last_name}'
#     return data
#

##Try it:
"""Write a function called find_bigger that accepts two decimal number and returns the bigger of the two"""
# def find_bigger(a = 0, b = 0):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     return f"There is no bigger number"
#
# # result = find_bigger(0, 0.8)
# result = find_bigger(b = 5, a = 6)
# print(result)


##Slide 33
"""Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise."""
# Returns True only is a string is a valid integer
# def only_ints(a,b):
#     # if a.is_integer() and b.is_integer():
#     #     return True
#     # return False
#
    # if str(a).isnumeric()  and str(b).isnumeric():
    #     return True
    # return False


# result = only_ints(1, 3.14)
# print(result) # Returns False
#
# result = only_ints(1, 3)
# print(result) # Returns True
# #
# result = only_ints('one', 3)
# print(result) # Returns False
#
# result = only_ints([1,2,3], 3)
# print(result) # Returns False




# ##Slide 34
## Write a function that removes digits from a string and returns it back with only alphabetic characters.
# TRY IT - NO AI
# def remove_digits(word):
#     only_letters = ""
#
#     for char in word:
#         if not char.isnumeric():
#             only_letters += char
#
#     return only_letters
#
# password = input("Please enter a password")
# result = remove_digits(password)
# print(result)




##Slide 35
##Write a function that accepts an integer and returns the sum of its digits
# TRY IT - NO AI
# def sum_of_numbers(n : int):
#     value = str(n) # Turns int into an iterable string
#
#     sum_of_digits = 0
#
#     for digit in value:
#         to_int = int(digit)
#         sum_of_digits += to_int
#
#     return sum_of_digits
#
# result = sum_of_numbers(901)
# print(result)


##Practice - Write a function that accepts an integer and returns a list of its factors.
def factors(n):
    factors_lst = []

    for i in range(1, n+1):
        if n % i == 0:
            factors_lst.append(i)

    return factors_lst

result = factors(128)
print(result)


###########Extra Example
"""Write a function that takes an integer and returns all integers within a range whose sum of digits is equal to the integer passed in.
For example if 11 is passed in then 29,38,47,etc.. are returned because 2+9=11, 3+8=11, etc..."""
def numbers_with_digit_sum(target_sum, start=0, end=1000):
    result = []  # this will store the numbers we find

    for num in range(start, end):
        # find the sum of the digits
        digits = str(num)  # turn the number into a string
        total = 0
        for d in digits:
            total += int(d)  # add each digit to the total

        # check if the total equals the target_sum
        if total == target_sum:
            result.append(num)

    return result

sum_lst = numbers_with_digit_sum(21)
print(sum_lst)
