alienDescription = {'color': 'grey', 'points': 10}

print(alienDescription['color'])
print(alienDescription['points'])

alienDescription['x-position'] = 0
alienDescription['y-position'] = 50

print(alienDescription)

print(alienDescription['color'])
alienDescription['color'] = 'green'

print("The aliens color is " + alienDescription['color'] + '.')

del alienDescription['y-position']
print(alienDescription)

favoriteLanguages ={
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby'
}

language = favoriteLanguages['jen'].title()
print("Jens favorite language is " + language + '.')

# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

lis = {'firstname': 'Lis', 'lastname': 'James', 'age': '27', 'city': 'Richmond'}

print(lis['firstname'])
print(lis['lastname'])
print(lis['age'])
print(lis['city'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favoriteNumbers = { 'friend1': 'lis', 'lisNumber': 1, 'friend2': 'steven', 'stevenNumber': 2, 'friend3': 'james', 'jamesNumber': 3, 'friend4': 'jack', 'jackNumber': 4, 'friend5': 'sarah', 'sarahNumber': 5}

print(favoriteNumbers['friend1'] + " favorite number is " + str(favoriteNumbers['lisNumber']) + ".")
print(favoriteNumbers['friend2'] + " favorite number is " + str(favoriteNumbers['stevenNumber']) + ".")
print(favoriteNumbers['friend3'] + " favorite number is " + str(favoriteNumbers['jamesNumber']) + ".")
print(favoriteNumbers['friend4'] + " favorite number is " + str(favoriteNumbers['jackNumber']) + ".")
print(favoriteNumbers['friend5'] + " favorite number is " + str(favoriteNumbers['sarahNumber']) + ".")

pythonDictionary = {'append': 'add to a list or dictionary',
                    'delete':'function to remove a item from a list or dictionary',
                    'sort': 'used to permanantly sort a list',
                    'list': 'used to store values of same type',
                    'insert': 'used to insert a value inbetween a list'}

appendKey = pythonDictionary.get('append')
print("Append: \n " + pythonDictionary['append'] + ".")
print("Delete: \n " + pythonDictionary['delete'] + ".")
print("Sort: \n "  + pythonDictionary['sort'] + ".")
print("List: \n " + pythonDictionary['list'] + ".")
print("Insert: \n" + pythonDictionary['insert'] + ".")

for key, value in pythonDictionary.items():
    print("Key: " + key)
    print("Value: " + value)

    pythonDictionary = {'append': 'add to a list or dictionary',
                        'delete': 'function to remove a item from a list or dictionary',
                        'sort': 'used to permanantly sort a list',
                        'list': 'used to store values of same type',
                        'insert': 'used to insert a value inbetween a list'}

for word, definition in pythonDictionary.items():
    print(word.title() + " is defined as " + definition + ".")

for word in pythonDictionary.keys():
    print(word)