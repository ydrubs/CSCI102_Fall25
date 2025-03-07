##Slide 5 - One way selection statement

# name = input("Enter your username: ")
# if name == 'admin':
#     print("Access granted - secret area unlocked")
#
# print()
# print("Welcome feel free to explore ")



#Slide 6 - If/else statement
# name = input("Enter your username: ")
# if name == 'admin':
#     print("Access granted - secret area unlocked")
# else:
#     print("Incorrect username")
#
# print("Other code")


##Slide 7: Multi-way selection
# number = int(input('Enter the numeric grade: '))
# if number > 89:
#     letter = 'A'
#     print('here1')
# if number > 79:
#     letter = 'B'
#     print('here2')
# elif number > 69:
#     letter = 'C'
# else:
#     letter = 'F'
# #
# print(f'The letter grade is {letter}')


# print("What color is the traffic light?")
# trafficLight = input("(r)ed, (y)ellow, or (g)reen: ")
#
# if (trafficLight == 'r') or (trafficLight == 'red'):
#     print("Stop!")
# elif (trafficLight == 'y') or (trafficLight == 'yellow'):
#     print("Hit the Gas!!!")
# elif (trafficLight == 'g') or (trafficLight == 'green'):
#     print("Go ahead.")
# else:
#     print("Check your vision, but drive like Mario Kart!")


##Slide 8 ACTIVITY



##Slide 9
# x = 10
# y = 5
# z = 2
#
# print(x == y) # False
# print(x > y) # True
# print(y > x/z) # False
# print(x.__ne__(y)) # True but don't worry about this
# print(x != y)

##Slide 11
# a = True
# b = False

#
# print(a or(a and b)) # True
# print(b and (a or b)) # False
# print(not b or (a and b)) # True
# print(a and not b or b and not a) # True
#
# #Write your own challening logic statement, make it as long as you want
# print(a and not b or b and not a or (a and not b)) # True



##Slide 11
# x = 40
# y = 20
# print(x == y or x == 2*y) # True
# print(x > y and x > 2*y)
# print(not(x == y or x == 2*y))

##slide 12
# grade = int(input("What is your grade: "))
# if grade >=90 and grade < 101:
#     print('Nice Job')
# elif grade < 90 and grade >= 80:
#     print('Not bad')
# elif pass:
#     print('There is room for improvement')
# else:
#     print("Better luck next time")

## WRAP UP ACTIVITY
# valid_username = 'user123'
# is_active = False
#
# user = input("Enter a username: ")
# if user == valid_username and is_active:
#     print("access granted")
# elif user == valid_username and not is_active:
#     print("access denied")
# else:
#     print('No user found')


##Slide 15
a = 4
b = 'hello'

# for number in range(a):
#     print(number, 'hello')
#     number = number+1
#     print(number)

# for n in b:
#     if n != 'h':
#         print(n)

##Slide 17
# number = 1
# for i in range(4):
#     print(number)
#     number = number + 3
#
# print(number)


##Slide 18
# number = 1
# times_2 = 2
# print(number)
#
# for i in range(5):
#     number = number * times_2
#     print(number)

##Slide 19
# for i in range(11):
#  print(i, end = '**')

# print()
##Equivelant to the following but twice as long
# count = 0
# for i in range(11):
#     print(count, end='**')
#     count = count + 1

##Checkpoint Activity
"""
Write a for loop that counts 20 ‘Mississippis’, such as -
1 Mississippi
2 Mississippi
...
...
20 Mississippi
"""""
# for i in range(1,21):
#     print(i, 'Mississippi')

##Slide21
# for i in range(1,21, 5): # First argument is starting number, second is ending, third is count by
#     print(i)
#
# for i in range(50,101):
#     print(i)

##SLide 22
#Count by threes
# for i in range(1,100,3):
#     print(i)

#Count backwards from 100
# for i in range(100,-1,-1):
#     print(i)


##Slide 23
# a = 5
# b = 5
# print(a, b)

# a += 5
# b -= 2
# print(a, b)


# c = 2
# d = 3
# print(c, d)

# c *= 5
# d **= 2 #Square the d variable
# print(c, d)

### FIZZ BUZZ Exercise (in-class)
# for i in range(1, 101):
#     # print(i)
#     if i %3 == 0 and i %5 == 0:
#         print('FizzBuzz')
#
#     elif i %3 == 0:
#         print("Fizz")
#     elif i %5 == 0:
#         print('Buzz')
#
#     else:
#         print(i)




##Slide 26
""" Ask for a number and add until you hit 1000 """
# stop = 1000
# total = 0
#
# while total < stop: # while loop is an entry-controlled loop
#     n = int(input("Please enter a number to add to the total: "))
#     total += n
#     print(total)


##slide 28 ACTIVITY
# stop = 1000
# total = 0
# step = float(input("Enter the step count: "))
#
# while total < stop:
#     print(round(total,1))
#     total += step
#
# print('Done')




##Slide 29
# theSum = 0.0
# data = input('Enter a number or just enter to quit: ')
# #
# while data != '':
#     number = float(data)
#     theSum += number
#     data = input('Enter a number or just enter to quit: ')
#     print('The sum is', theSum)


##Slide 30
# theSum = 0.0
# while True:
#     data = input("Enter a number or just enter to quit: ")
#     if data == 'stop':
#         break
# #
#     number = float(data)
#     theSum += number
#     print("The sum is", theSum)

##Slide 32
# while True: # Runs forever (until break)
#     number = int(input("Enter the numeric grade: "))
#     if number >= 0 and number <=100:
#         break
#
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input


##Slide 33
# done = False
# #
# while not done:
#     number = int(input("Enter the numeric grade: "))
#     if number >= 0 and number <= 100:
#         print("Setting 'done' to True")
#         done = True
# #
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input


#Slide 34
# Fail to break loop
# while True:
#     number = int(input('Enter the numeric grade: '))
#     if number >= 0 and number <= 100:
#         print(number)
#         # NEED TO ADD 'break'
#
#     else:
#         print('Error: grade must be between 100 and 0')
#         print(number) # Just echo the valid input

################infinite Loop, not updating variable
# a = 0
# count = 0
# while a < 1000:
#     count += 1
#     print(a, count)

###############Did not test for a = 500 condition
# a = 0
#
# while a < 1000:
#     a +=1
#     if a < 500:
#         print("Boom", a)
#     if a > 500:
#         print('Pow', a)
    ###Doesn't test a = 500


##Slide 35
# import random
# n = random.random()
# print(n)

# from random import randint # Don't have to reference random this way
# n = randint(1,100)
# print(n)




##Slide 36
##Dice rolling simulator - generate 10 random numbers between 1 and 6
# from random import randint
#
# for i in range(10):
#     print(randint(1,6), end = ' ,')
#
#     # Richy's 8-ball spectaculaer
#     n = randint(1,8)
#     if n == 7:
#         print('Absolutely')



# ##Guess the number game
# import random
#
# myNumber = random.randint(1,100)
# count = 0
# #
# while True:
#     count += 1
#     userNumber = int(input("Enter your guess: "))
#     if userNumber < myNumber:
#         print("Too small!")
#     elif userNumber > myNumber:
#         print("Too large!")
#     else:
#         print("Congratulations! You've got it in", count, "tries!")
#         break
