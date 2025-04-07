##Slide 5 - Defining lists
# fruits = ['apples', 'oranges', 'cherries']
# profile = [24, 3.2, 'hello', True]
# coordinates = [[-3,1], [0,3]]
# freinds = [] # Empty list
#
# print(len(fruits))
# print(fruits[1]) # Will say oranges
# print(profile[-1]) # Will say True
#
# print(coordinates[0][0]) # Gives -3 because that is the first element in the first sub-list

##Storing the result of a math operation in a list
# import math
# x = 2
# lst = [x, math.sqrt(2), round(math.pi, 2), x+1]
# print(lst)
# print(lst[1])
# print(lst[x+1]) # Gives three BECAUSE the element in positon 3 is equal 3

#Slide 6 - Your turn


##Slide 7
import random
# first = [1,2,3,4]
# second = list(range(1,53))
#
# print(max(first)) # Gives 4
# print(min(first)) # Gives 1
# print(sum(second))


# print(first) #returns the biggest value in the list
# print(second) #returns the smallest value in a list
# print(second[random.randint(1,53)])

##Build a list from a string
# message = 'Hello There How Are you Today'
# message_lst = list(message)
# print(message_lst)


# #Other list operations
# print(len(message_lst)) #chek the number of elements in a list
# print(message_lst + list('freind')) #Combine two lists together with a '+' sign


#Slide 8
##This example allows you to add people to a roster by looping through the number of people that get added
# roster_size = int(input("Enter the number of people to add: ")) #Get input about number
# roster_lst = [] #Create an empty list to hold the people
# #
# for i in range(roster_size): #Loop through however many people we said we wanted to add
#     new_member = input("What is the new members name? ") #Get the persons name
#     roster_lst.append(new_member) #Add the person to the end of the roster list
# #
# print(roster_lst) #print results


##This example generates n random numbers between 1 and 365 and puts them into a list
# from random import randint
# number_lst = [] #empty list to hold numbers
# n = 21 #How much elements to put in the list
#
# for i in range(n):
#     number = randint(1,365)#Choose random number
#     number_lst.append(number) #append that number to list
#
# print(number_lst)
# number_lst = set(number_lst)
# print(number_lst)
# print(len(number_lst))




##Slide 10 - Skill Review for exercise 5.1
##Stopping a loop when the 'enter' key is pressed.
# while True:
#     data = input("Enter some data: ")
#     if data == '':
#         break




#Slide 12 - Different operations and list slicing techniques that are possible
first = [1,2,3,4]
print(len(first))
print(first[0])
print(first[2:4])
first = first + [5,
                 6
                 ]

print(first)
#
# second = list(range(1,7))
# print(second)
# print(first == second) #True because elements are not the same
# print(first is second) #False because not the same place in memory


##Searching through a list
print(1 in first) # find an element in a list, TRUE
print('1' in first) # FALSE
print(int('1') in first) # TRUE
print(str(1) in first) # FALSE

# import random
# csci102_Roster = ['Osvaldo', 'Serena', 'Stephen', 'Garret', 'Miguel', 'Antonio', 'Conder', 'Jay', 'Jaden', 'Angel',
#                   'Melissa', 'Jaycen', 'Anthony', 'DaSean', 'Esteffan', 'Jeffery', 'Nicolas', 'Nguyen', 'Richy',
#                   'Gabriel', 'Jon', 'Vinnie', 'Ray']
# random_student = pass
# print(pass)
# print(pass)
#
# print(pass} extra credit points go to {random_student}')


##Slide 13 - Changing elements in a list
# first = [1,2,3,4]
# pass
# print(first)

# pass
# print(pass)


##Slide 14 - Manipulating through looping
# numbers = [2,3,4,5]
# pass
#     pass
# print(numbers)

# sentence = "Python is a good beginner programming language"
# sentence = sentence.split() #Split into individual words and make a list
# print(f"The sentence is {len(sentence)} words.")

#pass #Loop through each element by index
#     pass #Change each word to upper case and save it into the same position
# print(sentence)


##Slide 15 - adding elements by index
# pass
# pass
# print(csci102_Roster)

# pass
# print(csci102_Roster)


# new_students = ['Larry', 'Curley', 'Moe']
# pass
# print(csci102_Roster)

##Slide 16 - removing elements
# pass
# print(last_person)
#
# pass
# print(first_person)
#
# print(csci102_Roster)

##Remove an element using its name
# pass
# pass
# print(pos, new_freind)

##Slide 19 - searching and sorting
##Building a list from conditions in another list (numbers greater then 15)
# from random import randint
#
# lst = []
# for i in range(20):
#     lst.append(randint(1,20))
#
# new_lst = []
# pass
#     pass
#         pass
#
# print(new_lst)

##Slide 20
##Given a list of 20 random integers between 1 and 20, create a new list of all integers that appear more then once.
# from random import randint
#
# lst = []
# for i in range(20):
#     lst.append(randint(1,20))
#
# new_lst = []
# pass
#     pass
#         pass
#
# print(pass)
# print(pass)

##Given TWO lists of random numbers between 1 and 20 create a new list that has the common elements of both lists
# lst2 = []
# for i in range(20):
#     lst2.append(randint(1,20))
#
# print(lst)
# print(lst2)
#
# new_lst = []
# pass
#     pass
#         pass
#         pass
#
# print(new_lst)

##Slide 21 - Sorting a list
# lst = [4,10,2,1,7]
#
# pass
# print(lst)
#
# lst2 = [4,10,2,1,7]
#
# print(pass) # This returns the list sorted in numeric order
# print(lst2) #Notice that this returns the original list - not the sorted one
#
# lst3 = pass
# print(lst3)
#
# print(pass)



##Slide 23 - Intro to Tuples
# cards = pass #Empty tuple container
# cards = (6,7,8,9,10,'Jack') #Tuples of card ranks
# cards = ((2,'hearts'), (8, 'spades'), ('Ace', 'Clubs')) #Tuple of tuples
# cars = ([2020, 'Chevy', 'Corvette'], [2023, 'Toyota', 'Prius']) #Tuple of lists


# pass #Demonstrates you can't modify a tuple like you can a list

# pass #Since the third element [2] in the first tuple is a list, it can be modified. We are not modifying the tuple itself
# print(cars)


##SLide 25
###Building a deck of cards by combining tuples
# import random
#
# suit_tuple= ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8','9', '10', 'jack', 'queen', 'king', 'ace')
#
# deck = []
# pass
#     pass
#         pass #Temporary variable to store the current card in loop
#         pass #Add this card to the deck list
#         pass
#
# print(deck)

##Slide 26 (IN_CLASS_TUPLE PRACTICE)


##Slide 28
##Defining a simple function




##Slide 29
##Pass arguments into a function (no limit on amount or data type)






##Slide 30
##Pass default values into a function (order of keyword parameters vs. positional parameters matters!)
##positional parameters need to be defines FIRST!




##Try it:
"""Write a function called find_bigger that accepts two decimal number and returns the bigger of the two"""


##Slide 31
"""Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise."""







# ##Slide 32
##Write a function that removes digits from a string and returns it back with only alphabetic characters.






##Slide 33
##Write a function that accepts an integer and returns the sum of its digits







###########Extra Example
"""Write a function that takes an integer and returns all integers within a range whose sum of digits is equal to the integer passed in.
For example if 11 is passed in then 29,38,47,etc.. are returned because 2+9=11, 3+8=11, etc..."""

# def sum_digits(number):
#     for i in range(10,200):
#         current_number = list(str(i))
#         # print(current_number)
#         sum = 0
#         for digit in current_number:
#             sum += int(digit)
#             if sum == number:
#                 print(i)
#
# sum_digits(11)
