cars = ['bmw', 'audi', 'toyota', 'mercedes', 'nissan', 'lexus']
for car in cars:
    if car == 'bmw':
        print('True')
        print(car.upper())
    if car != 'bmw':
        print(car.title())

newCar = 'bmw'
newCar == 'bmw'

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

food = 'cookies'

if food == 'cookies':
    print("This is cookies.")
elif food != 'cookies':
    print("This is not cookies.")

if food.lower() == 'cookies':
    print("This is lower.")
if food.lower() != 'cookies':
    print("This is not cookies")

numbers = 19
if numbers > 20:
    print(str(numbers) + " is greater than 20.")
elif numbers < 20:
    print(str(numbers) + " is less than 20.")
elif numbers == 19:
    print(str(numbers) + " is equal to  19.")
elif numbers != 19:
    print(str(numbers) + " is not equal to 19.")
elif numbers <= 20:
    print(str(numbers) + " is less than/equal to 20.")
elif numbers >= 20:
    print(str(numbers) + " is greater than/equal to 20.")

