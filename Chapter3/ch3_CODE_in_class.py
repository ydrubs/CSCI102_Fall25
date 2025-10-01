##Slide 5 - One way selection statement
# name = input("Enter your username: ") # Assign user input to the 'name' variable
import random

# if name == 'admin':
#     print("Access granted.")
#
# print() # Blank line
# print("Welcome normal person!")


#Slide 6 - If/else statement
# name = input("Enter your username: ") # Assign user input to the 'name' variable
#
# if name == 'admin':
#     print("Access granted.")
# else:
#     print("Incorrect username")
#
# print("Loser, Caleb like cars!")



##Slide 7: Multi-way selection
# number = int(input('Enter the numeric grade: '))
# if number > 89:
#     letter = 'A'
# elif number > 79:
#     letter = 'B'
# elif number > 69:
#     letter = 'C'
# else:
#     letter = 'F'
#
# print(f"The letter grade is {letter}")



## Combining logic with a conditional
# print("What color is the traffic light?")
# trafficLight = input("(r)ed, (y)ellow, or (g)reen: ")



##Slide 8 ACTIVITY
# responce = input("How are you feeling today: ")
#
# if responce == 'tired':
#     print("go to sleep!")
#     prod_more = input("WHat's wrong")
#     if prod_more == 'did not sleep':
#         print("sleep now")
#     if prod_more == 'in Drubinskiys class':
#         print('Sorry')
#
# elif responce == 'happy':
#     print("Good for you")
# elif responce == 'sad':
#     print("i hope you feel better")
# else:
#     print("Well ooooookay")



##Slide 9
# x = 10
# y = 5
# z = 2
#
# print(x == y) # FALSE
# print(x == y + y) # True
# print(x > y) # True
# print(x > x/z) # True
# print(x != y) # True
# print(y >= x/z) #True




##Slide 11
# a = True
# b = False
#
# print(a or (a and b)) # True
# print(b and (a or b)) # False
# print(a and not b or b and not a) # True
#
#
# # #Write your own challening logic statement, make it as long as you want
# print(b or a and not b or a and b and not a or (a and not b)) # True
# print(b or (a == b) and a or not b and a and not b) # True



##slide 12 - Evaluating Logic statements
# grade = int(input("What is your grade: "))
#
# if grade >=90 and grade < 101:
#     print('Nice job')
# elif 90 > grade >= 80:
#     print('not bad')
# else:
#     print("there is room to improve")


## Slide 13 Activity





##Slide 16 - using a for loop
a = 4
b = 'hellhksdlkjslkjdhhhhhhhhho'

# for i in range(4): #Count -controlled loop
#     print(i, b)
#
# print('The last loop count was', i)
# print("The loop ran" , i + 1, 'times')

# for letter in b: # Looping over an iterable
#     print(letter)


## using a conditional in a for loop
# for letter in b:
#     if letter != 'h' and letter != 'l':
#         print(letter)



##Slide 18  - Looping through an algorithm
number = 1

# for i in range(100):
#     print(number)
#     number = number + 3

# count = 0
# while True:
#     print(count, number)
#     number = number + 3
#     count = count + 1
#


##Slide 19 - Another example
# n = 1
# multiply_by = 12

# print(n)
# for i in range(5):
#     print(n)
#     n = n * multiply_by
#
# print(n)


##Slide 20 - Using the loop counter in the loop
# for i in range(10):
#     print(i + 1 , end = ' ')



##Equivelant to the following but twice as long




##Checkpoint Activity
"""
Write a for loop that counts 20 ‘Mississippis’, such as -
1 Mississippi
2 Mississippi
...
...
20 Mississippi
"""""

# for i in range(21):
#     print(i, "Mississippi")




## Slide22 - Controlling the loop range
# for i in range(1,10): # First number is where the count starts, second number is one less then where it stops
#     print(i)
#
# for i in range(50,101):
#     print(i)





##SLide 23 - Controlling the loop range; counting by...
## Count by threes
# for i in range(3, 101, 3):
#     print(i)
#
#
# print()

## Count backwards from 100
# for i in range(100, 1, -1):
#     print(i)



##Slide 24 - Augmented Assignment
# a = 17
# b = 13
#
# a +=5 # same as a = a + 17
# b -=2 # same as b = b - 2
# print(a, b)
#
#
# c = 2
# d = 3
#
# c *=5
# d **=2
# print(c, d)



### FIZZ BUZZ Exercise (in-class)
# n = 42675
# print(n % 15)

# for i in range(1,101): #Count - controlled loop
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%5 == 0:
#         print("Fizz")
#     elif i%3 == 0:
#         print("Buzz")
#     else:
#         print(i)




##Slide 27 - The while Loop
""" Ask for a number and add until you hit 1000 """
# stop = 1000
# total = 0
# step = float(input("Please enter a number: "))
#
# while total <= stop: # while loop is an entry-controlled loop
#     print(total)
#     total += step # same as total = total + stop


##slide 29 ACTIVITY
# stop = 1000
# total = 0
#
# while total < stop:
#     n = int(input("How much do you want to add: "))
#     total +=n
#     print(total)





##Slide 30 - While Loop for entering data
# theSum = 0.0
# data = input('Enter a number or just enter to quit: ')
# print(data)
#
# while data != '':# Loop triggers if a string is not empty
#     number = float(data)
#     theSum += number
#     data = input("Enter a number, please: ")
#     print(theSum)




##Slide 31 - Breaking a loop
# theSum = 0.0
#
# while True:
#     data = input('Enter a number or just enter to quit: ')
#     if data == 'stop':
#         break
#
#     number = float(data)
#     theSum += number
#     print(theSum)




##Slide 33 - While loop to validate data

# while True: # Runs forever (until break)
#     number = int(input("Enter a number between 0 and 100, please: "))
#     if number >=0 and number <=100:
#         print("thanks")
#         break
#
#     else:
#         print(f"Error, the number is out of range, you put in {number}")






## Slide 34 - The While and the Boolean flag
# done = False
#
# while not done:
#     number = int(input("Enter a number between 0 and 100, please: "))
#     if number >=0 and number <=100:
#         print("setting done to True")
#         done = True
#
#     else:
#         print(f"Error, the number is out of range, you put in {number}")


## Slide 35 - Common while loop logic errors
##  Fail to break loop

# while True:
#     number = int(input('Enter the numeric grade: '))
#     if number >= 0 and number <= 100:
#         print(number)
#         # NEED TO ADD 'break'
#         # break
#
#     else:
#         print('Error: grade must be between 100 and 0')


################infinite Loop, not updating variable
# a = 0
# count = 0
# while a < 1000:
#     count += 1
#     print(a, count)

# while True:
#     count +=1
#     print(a, count)
#     if count > 1000:
#         break

###############Did not test for a = 500 condition
# a = 0
#
# while a < 1000:
#     a +=1
#     if a < 500:
#         print("Boom", a)
#     if a > 500:
#         print('Pow', a)
#     #Doesn't test a = 500
#     if a == 500: #FIX
#         print('Here ' * 10)


##Slide 36 - Importing Modules -> Random
# import random
# n = random.random()
# print(n)
#
# m = random.randint(1,20)
# print(m)


# from random import randint, random # Don't have to reference random this way
# n = randint(1,20)
# m = random()
# print(n, m)





##Slide 37
##Dice rolling simulator - generate 10 random numbers between 1 and
# from random import randint
#
# number_of_dice = 10
#
# for i in range(number_of_dice):
#     d6 = randint(1,6)
#     d20 = randint(1,20)
#
#     print(f"D6 {d6}, D20 {d20}")



## Guess the number game
# import random
# from random import randint
#
# computer_number = randint(1,100)
# counter = 0
#
# while True:
#     counter += 1
#     user_number = int(input("Guess a number between 1-100"))
#
#     if user_number < computer_number:
#         print("Too small")
#     elif user_number > computer_number:
#         print("Too big")
#     else:
#         print(f"You got it in {counter} guesses.")
#         break

# In-class Exercise (coinflip)
from random import randint

flip_count = 0
head_count = 0

while head_count < 10:
    flip_count +=1
    result = randint(0,1)

    if result == 0: # 0 means heads
        head_count +=1
        # print("You rolled heads, yay!")
    else:
        head_count = 0

print(f"It took you {flip_count} flips to get three heads in a row.")