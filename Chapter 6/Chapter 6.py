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

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

pythonDictionary = {'append': 'add to a list or dictionary',
                        'delete': 'function to remove a item from a list or dictionary',
                        'sort': 'used to permanently sort a list',
                        'list': 'used to store values of same type',
                        'insert': 'used to insert a value inbetween a list',
                        'print': 'used to print strings ',
                        'for loop': 'used to iterate through a list or dictionary',
                        'if-else statement': 'used to create a conditional statements',
                        'dictionary': 'used to store values of different types.',
                        'tuple': 'used to store values of same type cannot be edited in anyway.'}

for word, definition in pythonDictionary.items():
    print(word.title() + ": " + definition + ".")


# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.

famousRivers = {'amazon river': 'brazil', 'nile river': 'egypt', 'mississippi river': 'usa'}
for river, country in famousRivers.items():
    print(river.title() + ' runs through ' + country.title() + '.')

for river in famousRivers.keys():
    print(river)

for country in famousRivers.values():
    print(country)

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }

peoplePoll = ['jen', 'sarah', 'edward', 'phil', ' rachel','jacob','steven','thomas',
    'lis']

for people in peoplePoll:
    if people in favorite_languages.keys():
       print(people + ' poll already taken')
    if people not in favorite_languages.keys():
       print(people + ' please take poll')

# list of dictionaries

person1 = {'name': 'lis', 'ethnicity': 'indian'}
person2 = {'name': 'james', 'ethnicity': 'indian'}
person3 = {'name': 'mark', 'ethnicity': 'french'}
person4 = {'name': 'jacob', 'ethnicity': 'spanish'}

persons = [person1, person2, person3, person4]
print(persons)

for person in range(30):
