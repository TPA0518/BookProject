message = input("Tell me something that I want to know: ")
print(message)


message = "If you tell us who you are we will send you a message. "
message += "What is your name?"

name = input(message)
print( "Hello, " + name)

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
