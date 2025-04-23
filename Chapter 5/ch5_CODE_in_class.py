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
# first = [1,2,3,4]
# print(len(first))
# print(first[0])
# print(first[2:4])
# first = first + [5,
#                  6
#                  ]
#
# print(first)
#
# second = list(range(1,7))
# print(second)
# print(first == second) #True because elements are not the same
# print(first is second) #False because not the same place in memory


## Searching through a list
# print(1 in first) # find an element in a list, TRUE
# print('1' in first) # FALSE
# print(int('1') in first) # TRUE
# print(str(1) in first) # FALSE

#
# import random
csci102_Roster = ['Osvaldo', 'Serena', 'Stephen', 'Garret', 'Miguel', 'Antonio', 'Conder', 'Jay', 'Jaden', 'Angel',
                  'Melissa', 'Jaycen', 'Anthony', 'DaSean', 'Esteffan', 'Jeffery', 'Nicolas', 'Nguyen', 'Richy',
                  'Gabriel', 'Jon', 'Vinnie', 'Ray']
# random_student = random.choice(csci102_Roster)
# print(random_student)
# print('Bob' in csci102_Roster) # False
# #
# print(f'{random.randint(-10,10)} extra credit points go to {random_student}')


##Slide 13 - Changing elements in a list
# first = [1,2,3,4]
# first[0] = 5
# print(first)
#
# csci102_Roster[0] = 'Taylor Swift'
# print(csci102_Roster)


##Slide 14 - Manipulating through looping
# numbers = [2,3,4,5]
# for i in range(len(numbers)): # Looping using the index of the list
#     numbers[i] = numbers[i] ** 2
# print(numbers)
#
# n_lst = []
# for number in numbers:
#     n_lst.append(number**2)
# print(n_lst)

# sentence = "Python is a good beginner programming language"
# sentence = sentence.split() #Split into individual words and make a list
# print(sentence)
# print(f"The sentence is {len(sentence)} words.")
#
# for i in range(len(sentence)): #Loop through each element by index
#     sentence[i] = sentence[i].upper() #Change each word to upper case and save it into the same position
# print(sentence)


##Slide 15 - adding elements by index, without replacing data
# csci102_Roster.insert(1, "Adam Sandler")
# print(csci102_Roster)
# csci102_Roster.insert(3, "Soulja Boy")
# print(csci102_Roster)
#
# new_students = ['Larry', 'Curly', 'Moe']
# csci102_Roster.extend(new_students)
# csci102_Roster = csci102_Roster + new_students # Does the same thing as the line above


##Slide 16 - removing elements
# print(csci102_Roster[-1])
# last_person = csci102_Roster.pop()
# print(last_person)
# #
# first_person = csci102_Roster.pop(0)
# print(first_person)


##Remove an element using its name
# some_person = csci102_Roster.index("Stephen")
# print(some_person)
#
# if 'DaSean' in csci102_Roster:
#     other_person = csci102_Roster.index("DaSean")
#     print(other_person)
#     best_student = csci102_Roster.pop(other_person)
#     print(best_student)
# else:
#     print('Bob is not ont he list')

##Slide 20 - searching and sorting
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

##Slide 21
##Given a list of 20 random integers between 1 and 20, create a new list of all integers that appear more then once.
# from random import randint
# #
# lst = []
# for i in range(20):
#     lst.append(randint(1,20))
# print(lst)

# new_lst = []
# for number in lst:
#     if lst.count(number) > 1:
#         if number not in new_lst:
#             new_lst.append(number)

# new_lst = set(new_lst)
# print(sorted(lst))
# print(sorted(new_lst))

##Given TWO lists of random numbers between 1 and 20 create a new list that has the common elements of both lists
# lst2 = []
# for i in range(20):
#     lst2.append(randint(1,20))
# #
# print(lst)
# print(lst2)
# #
# new_lst = []
# for number in lst:
#     if number in lst2:
#         new_lst.append(number)
#         lst2.pop(lst2.index(number))
# #
# print(new_lst)


##Slide 22 - Sorting a list
# lst = [4,10,2,1,7]
# #
#
# lst.sort()
# lst.sort(reverse=True)
# print(lst)


# letters = ['c', 'h', 'b', 'A', 'M', 'B']
# letters.sort()
# print(letters)
# print(ord('A'), ord('a'))

# lst2 = [4,10,2,1,7]
#
# sorted(lst2) # This returns the list sorted in numeric order
# print(lst2) #Notice that this returns the original list - not the sorted one
# #
# lst3 = sorted(lst2)
# print(lst3)
#




##Slide 24 - Intro to Tuples
# cards = () #Empty tuple container
# print(type(cards))
# cards = (6,7,8,9,10,'Jack') #Tuples of card ranks
# cards_full = ((2,'hearts'), (8, 'spades'), ('Ace', 'Clubs')) #Tuple of tuples
# cars = ([2020, 'Chevy', 'Corvette'], [2023, 'Toyota', 'Prius']) #Tuple of lists
#
# print(cards[3])
# print(cards_full[1])
# print(cars[1])
# cards = list(cards) # If we change the cards tuple to a list we can do the line below
# cards[0] = 'Ace' #Demonstrates you can't modify a tuple like you can a list, unless you run the line above
#
# cars[1][2] = 'Rav-4' #Since the third element [2] in the first tuple is a list, it can be modified. We are not modifying the tuple itself
# print(cars)


##SLide 26
### Building a deck of cards by combining tuples
import random
#
# suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8','9', '10', 'jack', 'queen', 'king', 'ace')
# #
# deck = []
# for suit in suit_tuple:
#     for rank in rank_tuple:
#         card = (rank, suit) #Temporary variable to store the current card in loop
#         # print(card) # Show the card for debugging
#         deck.append(card) #Add this card to the deck list

# print(len(deck))
# print(deck)
# random.shuffle(deck)
# print(deck)
#
# print(random.choice(deck))


##Slide 27 (IN_CLASS_TUPLE PRACTICE)
# point1 = (2,6)
# point2 = (-9,-10)
#
# x1 = point1[0]
# y1 = point1[1]
#
# x2 = point2[0]
# y2 = point2[1]
#
# slope = (y2-y1)/(x2-x1)
# print(round(slope,2))
#
# slope_alt = (point2[1] - point1[1])/(point2[0] - point1[0])
# print(slope_alt)


##Slide 29
##Defining a simple function
# def greeting():
    # return 'Hi everybody'
    # print('Hi Everybody')

# print(greeting()) # Need parenthesis to trigger the function
# say_hello = greeting()
# print(say_hello, type(say_hello))

# greeting()
# print(greeting())

##Slide 31
##Pass arguments into a function (no limit on amount or data type)
# def greeting(first_name, last_name): # first name and last name are considered POSITIONAL arguments
#     data = f"Call me {last_name}, {first_name}, {last_name}"
#     return data

# message = greeting('James', 'Bond')
# print(message)

# message = greeting() # If you call a function that expects parameters but does not get them, you get an ERROR
# print(message)





##Slide 32
##Pass default values into a function (order of keyword parameters vs. positional parameters matters!)
##positional parameters need to be defines FIRST!
# def greeting(first_name = 'John', last_name = 'Doe'): # These are KEYWORD Parameters
#     data = f"Call me {last_name}, {first_name}, {last_name}"
#     return data
#
# message = greeting() # Returns the default parameters
# print(message)
#
# message = greeting('James')
# print(message)
#
# message = greeting(last_name='James')
# print(message)
#
# message = greeting('James', "Bond")
# print(message)


## Using BOTH POSITIONAL and KEYWORD
# def greeting(first_name, last_name = 'Doe'): # These are KEYWORD Parameters
#     data = f"Call me {last_name}, {first_name}, {last_name}"
#     return data
#
# message = greeting('James')
# print(message)

# def greeting(first_name = "John", last_name): # ERROR because POSITIONAL comes before KEYWORD
#     data = f"Call me {last_name}, {first_name}, {last_name}"
#     return data

##Try it:
"""Write a function called find_bigger that accepts two decimal number and returns the bigger of the two"""
# def find_bigger(a,b):
#     if a > b:
#         return a
#     return b
#
# compare = find_bigger(2.17, 3.14)
# print(compare)


##Slide 33
"""Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise."""
# print('3'.isnumeric()) # Returns True only is a string is a valid integer

# def only_ints(a, b):
#     if str(a).isnumeric() and str(b).isnumeric():
#         return True
#     else:
#         return False
#
# result = only_ints(1, 3.14)
# print(result)






# ##Slide 34
## Write a function that removes digits from a string and returns it back with only alphabetic characters.
# def remove_digits(word):
#     new_word = ""
#     for char in word:
#         if not char.isnumeric():
#             new_word +=char
#
#     return new_word
#
# message = input("Enter a message")
# no_numbers = remove_digits(message)
# print(no_numbers)



##Slide 35
##Write a function that accepts an integer and returns the sum of its digits
def sum_digits(number):
    number = list(str(number))
    sum = 0
    for digit in number:
        sum += int(digit)

    return sum

print(sum_digits(123))




###########Extra Example
"""Write a function that takes an integer and returns all integers within a range whose sum of digits is equal to the integer passed in.
For example if 11 is passed in then 29,38,47,etc.. are returned because 2+9=11, 3+8=11, etc..."""
