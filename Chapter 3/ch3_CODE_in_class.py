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
a = True
b = False

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
valid_username = 'user123'
is_active = False

user = input("Enter a username: ")
if user == valid_username and is_active:
    print("access granted")
elif user == valid_username and not is_active:
    print("access denied")
else:
    print('No user found')


##Slide 15
# a = 4

# pass
# pass
# pass

##Slide 17
# number = 1
# pass
# pass
# pass

##Slide 18
# number = 1
# times_2 = 2
# for i in range(5):
#     number = number * times_2
#     print(number)

##Slide 19
# for
# pass


##Equivelant to the following but twice as long
# count = 0
# for i in range(11):
#     print(count, end=' ')
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


##Slide21
# pass
# pass


##SLide 22
#Count by threes

#Count backwards from 100

##Slide 23
# a = 5
# b = 5
# print(a, b)

# pass
# pass
# print(a, b)


# c = 2
# d = 3
# print(c, d)

# pass
# pass
# print(c, d)


# pass
# print(d)

##Slide 25



##slide 27 ACTIVITY





##Slide 28
# theSum = 0.0
# data = input('Enter a number or just enter to quit: ')
#
# while pass:
#     number = float(data)
#     theSum += number
#     data = input('Enter a number or just enter to quit: ')
#     print('The sum is', theSum)


##Slide 29
# theSum = 0.0
# while pass:
#     data = input("Enter a number or just enter to quit: ")
#     if data == pass:
#         pass
#
#     number = float(data)
#     theSum += number
#     print("The sum is", theSum)

##Slide 31
# while True:
#     number = int(input("Enter the numeric grade: "))
#     if pass:
#         pass
#
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input


##Slide 32
# done = False
#
# while not done:
#     number = int(input("Enter the numeric grade: "))
#     if number >= 0 and number <= 100:
#         print("Setting 'done' to True")
#         pass
#
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input


##Slide 33
#Fail to break loop
# while True:
#     number = int(input('Enter the numeric grade: '))
#     if number >= 0 and number <= 100:
#         print(number)
#
#     else:
#         print('Error: grade must be between 100 and 0')
#         print(number) # Just echo the valid input

################infinite Loop, not updating variable
# a = 0
# while a < 1000:
#     print(a)

################Did not test for a = 500 condition
# a = 0
# while a < 1000:
#     a +=1
#     if a < 500:
#         print("Boom", a)
#     if a > 500:
#         print('Pow', a)

##Slide 34
# pass
# pass
# pass


##Slide 35
##Dice rolling simulator
# pass
# pass
# pass


##Guess the number game
# import random
#
# myNumber = random.randint(1,100)
# count = 0
#
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
