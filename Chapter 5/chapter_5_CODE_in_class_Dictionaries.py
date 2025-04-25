##Slide 3
# people = {'Jon': 'Lawyer', 'Susan': 'Programmer', 'Robert': 'Bank Manager', 'Tanya': 'Engineer', 'Conder': 'Student'}
# print(people)
# print(type(people))

##SLide 4
# print(people[0]) #This will give an error because dictionaries are not ordered (can't access by index)
# print(people['Susan']) # This will return the value


# people = {'Jon': 'Lawyer', 'Susan': 'Programmer', 'Robert': 'Bank Manager', 'Tanya': 'Engineer', 'Jon':'Teacher'}
# print(people)

##Slide 5
# fords = {'Ford': 'Mustang', 'Ford': 'Fusion', 'Ford': 'F150', }
# print(fords)

##Slide 6
# We need to install the 'Faker' library first
import faker # Import faker

fake_id = faker.Faker() #Genearte a fake_id
profile = fake_id.profile() #Get a profile information from the fake id data set
# print(dir(fake_id))
# print(fake_id.ssn())

print(profile)

##Slide 7
# print(profile['job']) ##Access the value corresponding to a key
# print(profile['age']) #Gives an error because age is not a key in the dictionary

# You can also use .get to access values
# print(profile.get('job'))
# print(profile.get('age'))


##Slide 8
# print(profile.keys()) # Returns all the keys of the dictionary
# print(profile.values()) # Returns only the values
# print(profile.items())

##Slide 9
#Loop all the keys
# for key in profile.keys():
#     print(key)

#Loop all the values
for value in profile.values():
    print(value)



#Loop all the keys/value pairs and display as a tuple




##Slide 10
#Add entries to a dictionary




##Remove an entry by specifying a key




##Slide 11 - Your turn
# me = {}
# me['name'] = 'my_name'


##Slide 12
#Given a list of classes and a list of grades create a dictionary that links the data together
# courses = ['Trigonometry', 'Physics', 'Programming', 'English 2']
# grades = [85, 94, 98, 80]

# gradebook = {}

##Loop through the index of each course and associate the course as the key at that index to the grade as the value at the same index to the gradebook





#Find the average grade of all the classes





##Slide 13
# my_string = 'Hello, how are you'



##Slide 14 - Practice 1
"""Your task:Create a new dictionary that removes ‘ssn’, ‘blood_group’, and ‘birthdate’ from the previous dictionary and moves 
it into the new dictionary. Write the new dictionary into a variable called ‘private_data’
"""
profile = {'job': 'Clinical embryologist', 'company': 'Garcia and Sons', 'ssn': '101-48-3433',
           'residence': '115 White Field Suite 854 Port Josephmouth, NC 77328',
           'current_location': (-18.7254755, -86.461244), 'blood_group': 'A-',
           'website': ['https://wade-williams.com/', 'http://flores.com/'], 'username': 'arroyosusan',
           'name': 'Donna Gonzalez', 'sex': 'F', 'address': '8086 Warner Inlet Suite 223 New Jack, WI 37965',
           'mail': 'milesjessica@yahoo.com', 'birthdate': (1922, 1, 30)}
# print(profile)




##Slide 15 - Practice 2 (Optional Challenge
'''Your Task: Create a new dictionary that contains only the dictionary entries that are greater then 50.  
Start with the code below that generates a random numbers between 1 and 100 for every letter of the alphabet.
Then write a script that creates a new dictionary with key-value that have the value data greater then 50.'''

# from random import randint
# numbers = {}
# for i in range(ord('a'), ord('a')+26):
#     numbers[chr(i)] = randint(1,100)
#
# print(numbers)

