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

# print(profile)

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
# Loop all the keys
# for key in profile.keys():
#     print(key)

# #Loop all the values
# for value in profile.values():
#     print(value)



#Loop all the keys/value pairs and display as a tuple
# for key, value in profile.items():
#     print(key, value)



##Slide 10
#Add entries to a dictionary
# profile['nickname'] = 'Champ'
# print(profile)


##Remove an entry by specifying a key
# profile.pop('ssn')
# print(profile)
# print(profile['ssn']) # We get error now because 'ssn' is removed


##Slide 11 - Your turn
# me = {}
# me['name'] = 'my_name'
# me['Spirit Animal'] = 'Panda'
# print(me)
# me['Spirit Animal'] = 'Lion'
# print(me)


##Slide 12
#Given a list of classes and a list of grades create a dictionary that links the data together
# courses = ['Trigonometry', 'Physics', 'Programming', 'English 2']
# grades = [85, 94, 98, 80]
#
# gradebook = {}

##Loop through the index of each course and associate the course as the key at that index to the grade as the value at the same index to the gradebook
# for i in range(len(courses)):
#     gradebook[courses[i]] = grades[i]
# print(gradebook)

#Find the average grade of all the classes
# avg_grade = sum(gradebook.values())/len(gradebook.values())
# print(avg_grade)
# gradebook['average_grade'] = avg_grade
# print(gradebook)


##Slide 13
# my_string = 'Hello, how are you'
#
# char_dict = {}
#
# for i in range(len(my_string)):
#     char_count = my_string.count(my_string[i])
#     char_dict[my_string[i]] = char_count
#
# print(char_dict)


##Slide 14 - Practice 1
"""Your task:Create a new dictionary that removes ‘ssn’, ‘blood_group’, and ‘birthdate’ from the previous dictionary and moves 
it into the new dictionary. Write the new dictionary into a variable called ‘private_data’
"""
profile = {'job': 'Clinical embryologist', 'company': 'Garcia and Sons', 'ssn': '101-48-3433',
           'residence': '115 White Field Suite 854 Port Josephmouth, NC 77328',
           'current_location': (-18.7254755, -86.461244), 'blood_group': 'A-',
           'website': ['h ttps://wade-williams.com/', 'http://flores.com/'], 'username': 'arroyosusan',
           'name': 'Donna Gonzalez', 'sex': 'F', 'address': '8086 Warner Inlet Suite 223 New Jack, WI 37965',
           'mail': 'milesjessica@yahoo.com', 'birthdate': (1922, 1, 30)}
print(profile)

private_data = {} # New_Dictionary

private_data['ssn'] = profile['ssn']
profile.pop('ssn')
print(private_data)
print(profile)

private_data['blood_group'] = profile.get('blood_group') # This will return the value or None, NOT error
print(private_data)



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

