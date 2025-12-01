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



