message = input("Tell me something that I want to know: ")
print(message)

message = "If you tell us who you are we will send you a message. "
message += "What is your name?"

name = input(message)
print("Hello, " + name)

height = "Tell us how tall you are, in inches. "
myHeight = input(height)

if int(myHeight) >= 63:
    print("You are tall enough to ride this roller coaster. ")
else:
    print("You are unable to ride the roller coaster. ")

number = input("Enter a number, to determine if the number is even or odd.")

if int(number) % 2 == 0:
    print(number + " is an even number.")
elif int(number) % 2 == 1:
    print(number + " is an odd number.")

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

rentalCar = input("What kind of car would you like?")
print("Let me see if I can find you a " + rentalCar + ".")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

reservePeople = input("How many people are in your dinner group?")
if int(reservePeople) > 8:
    print("Im sorry, you'll have to wait for a table because you have a party of " + reservePeople + ".")
else:
    print("Your table is ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not

multNumberTen = input("Please enter a number")
if int(multNumberTen) % 10 == 0:
    print(multNumberTen + " is a multiple of ten.")
else:
    print(multNumberTen + " is not a multiple of ten.")

currentNumber = 0
while currentNumber <= 5:
    print(currentNumber)
    currentNumber += 1

prompt = "Tell me something and I will repeat it. Enter 'quit' to end the the program."
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active == True:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I love to go to " + city + ".")

currentNumber = 0
while currentNumber < 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue

    print(currentNumber)

x = 1
while x < 5:
    print(x)
    x += 1

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
prompt = "Enter a pizza toppings for your pizza."
prompt += "\nEnter 'quit' when you have finished entering toppings."
pizzaTopping = []
while True:
    message = input(prompt)
    if message == 'quit':
        print("We will add the following toppings to you pizza: ")
        for topping in pizzaTopping:
            print("-" + topping)
        print("We will make your pizza now.")
        break
    else:
        pizzaTopping.append(message)
        print("We will add that topping to your pizza.")

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket
prompt = "Enter your age we will give you the price of your ticket."
prompt += "\nEnter 'quit' when you have finished asking for pricing."
while True:
    message = input(prompt)
    if message == 'quit':
        print("If you need any help about pricing please ask.")
        break
    if int(message) < 3:
        print("The price of a ticket is for a person under than 3 is free.")
        continue
    if 12 >= int(message) >= 3:
        print("The price of a ticket is $10.")
        continue
    if int(message) > 12:
        print("The price of the ticket is $15.")
        continue

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.


# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# ctrl-C or close the window displaying the output.)