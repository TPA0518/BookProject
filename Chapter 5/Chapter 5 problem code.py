cars = ['bmw', 'audi', 'toyota', 'mercedes', 'nissan', 'lexus']
for car in cars:
    if car == 'bmw':
        print('True')
        print(car.upper())
    if car != 'bmw':
        print(car.title())

requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print('Hold the anchovies!')

answer = 21

if answer != 42:
    print("That is not the correct answer. Try again.")

age = 30
if age < 21:
    print("True")
elif age > 21:
    print("Not True")
else:
    print(False)

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •	 Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# •	 Create at least ten tests. Have at least five tests evaluate to True and
# another five tests evaluate to False.
#

bannedUsers = ['andrew', 'ahmed', 'david']
user = 'thomas'
if user not in bannedUsers:
    print(user.title() + ' is not a banned user.')

print(" Is user == thomas? I predict True.")
print(user == 'thomas')

print(" Is user == bob? I predict False.")
print(user == "bob")

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# •	 Tests for equality and inequality with strings
# •	 Tests using the lower() method
# •	 Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# •	 Tests using the and keyword and the or keyword
# •	 Test whether an item is in a list
# •	 Test whether an item is not in a list

food = 'Cookies'

if food == 'cookies':
    print("This is cookies.")
elif food != 'cookies':
    print("This is not cookies.")

if food.lower() == 'cookies':
    print("This is lowercase.")
if food.lower() != 'cookies':
    print("This is not cookies")

numbers = 30
numberCompare = 40
if numbers > numberCompare:
    print(str(numbers) + " is greater than " + str(numberCompare))
elif numbers < numberCompare:
    print(str(numbers) + " is less than " + str(numberCompare))

if numbers == numberCompare:
    print(str(numbers) + " is equal to " + str(numberCompare))
elif numbers != numberCompare:
    print(str(numbers) + " is not equal to " + str(numberCompare))

if numbers <= numberCompare:
    print(str(numbers) + " is less than/equal " + str(numberCompare))
elif numbers >= numberCompare:
    print(str(numbers) + " is greater than/equal " + str(numberCompare))

if numbers <= numberCompare and numbers >= 20:
    print(True)
else:
    print(False)
if numbers >= numberCompare or numbers >= 30:
    print(True)
else:
    print(False)

cars = ['bmw', 'audi', 'toyota', 'mercedes', 'nissan', 'lexus', 'subaru']
car = 'bmw'
car2 = 'subaru'
if car in cars:
    print(car.upper() + " found in the list")
else:
    print(car.upper() + " not found in list")

if car2 not in cars:
    print(car2.title() + " not found in list")
else:
    print(car2.title() + " found in list")

votingAge = 21
if votingAge >= 18:
    print("\nYou are old enough to vote.")
    print("\nHave you registered to vote?")
else:
    print("\nSorry, You arent old enough to vote.")
    print("\nPlease, when you are old enough please register.")

amusementAge = 20
if amusementAge < 4:
    print("\nYou are unable to ride. Admission cost is $0.")
elif amusementAge < 18:
    print("\nYou are able to ride. Admission cost is $25.")
else:
    print("\nYou are able to ride. Admission cost is $40.")

amusementAge = 20
if amusementAge < 4:
    price = 0
elif amusementAge < 18:
    price = 25
else:
    price = 40

print("Your admission cost is $" + str(price))




