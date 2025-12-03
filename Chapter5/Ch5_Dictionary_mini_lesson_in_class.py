"""
A DICTIONARY is a Python data type that links to pieces of data together inside of curly-brackets {}
    The first piece of data is called the KEY
    The second piece of data is called the VALUE
"""

#Define a dictionary
cars = {}
cars = {'Ford' : 'Fusion', 'Toyota' : 'Camry', 'Cadillac' : 'Escalade'}
print(len(cars))

# We can use the .keys() and the .values() method to view the keys and values separately
print(cars.keys())
print(cars.values())

# We can add to a dictionary by specifying the KEY and setting it equal to a value
cars['Chevy'] = 'Corvette'
print(cars)

# car_make = input('Enter a car make: ')
# car_model = input ('Enter a car model: ')
#
# cars[car_make] = car_model # Create a dictionary entry from user input
# print(cars)



#Dictionary are NOT ORDERED meaning we CAN'T use their INDEX to access them or manipulate them
# print(cars[0]) # Using an index number causes an ERROR
# cars [0] = 'Fiat' # This makes 0 a key in a dictionary
# print(cars)

# print(cars["ford"]) # ERROR because ford != Ford
print(cars["Ford"]) # Gives Fusion

#Create a dictionary using a loop
# for i in range(2):
#     car_make = input('Enter a car make: ')
#     car_model = input ('Enter a car model: ')
#     cars[car_make] = car_model
#
# print(cars)


# Dictionaries KEYS have to be UNIQUE, otherwise, the LAST entry will overwrite the previous similar one
cars["Ford"] = 'F150'
print(cars)

cars['Honda'] = ['Civic', 'Accord', 'S2000']
print(cars)



# We can perform operations on dictionary keys:
d = {'a': 13, 'b': 7, 'c' : 12}

print(sum(d.values())) # Add up all the values

# print(sum(d.keys()))# Error because can't add strings




# PRACTICE 12/3
# 1)Create a dictionary of states and their capital cities that includes:
#           1) Kansas – Topeka 2) Texas – Austin 3) Arkansas – Little Rock

# 2) Write a line of code that accesses and prints only capital cities in the above dictionary
# 2b) Add the state Nebraska and its capital Lincoln
# 3) Write a for loop that converts the city in each dictionary all capital letters and print the dictionary

places = {'Kansas': 'Topeka', 'Texas': 'Austin', 'Arkansas': 'Little Rock'}

# print(places.values())
#
# places['Nebraska'] = 'Lincoln'
# print(places)
#
# print(places['Kansas']) # THis returns the VALUE of the KEY

for city in places.values():
    # print(city)
    print(city.upper())

print(places.items())  # Returns key and value as a tuple

for state, city in places.items():
    print(state, city)
    city_upper = city.upper()
    places[state] = city_upper

print(places)
places['Kansas'] = 'Garden City'  # Overwrites Topeka with Garden City
print(places)

""" 4)	Explain - Why does the following cause an error: 

    colors = {'Red': 5, 'Blue': 3}
    print(colors[0])   # Error

    ANSWER: A dictionary is not ordered, so you can't index is entries using integers

"""

# WRAP UP QUESTION - Start two lists
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

d = {}

# for letter in l1:
#     print(letter)
#     d [letter] = ???

for i in range(len(l1)):
    k = l1[i]
    d[k] = l2[i]

print(d)



