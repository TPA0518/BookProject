# Iterating through an array states example.
states = ['maryland', 'rhode island', 'new jersey', 'california', 'oregon']

for state in states:
    print(state.title() + ", is a state I wish to visit.")
    print("I cant wait to go visit " + state.title() + ".")

print("These are all the states I want to visit.\n")

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

favoritePizza = ["Cheese Pizza", "Pepperoni Pizza", 'Pineapple Pizza']

for pizza in favoritePizza:
    print(pizza + "is my favorite pizza.")
print("I really like pizza.")

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# •	 Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

animals = ['dog', 'cat', 'lizard', 'aligator', 'rat']

for animal in animals:
    print("A " + animal + " would make a good pet.")

print("These animals all have four legs. ")

for value in range(1, 6):
    print("This is number " + str(value) + ".")

numbers = list(range(1, 11))
print(numbers)

evenNumbers = list(range(2, 51, 2))
print(sorted(evenNumbers, reverse=True))

cubed = []
for value in range(1, 11):
    cube = value ** 3
    cubed.append(cube)

print(cubed)

Numbers = list(range(1, 51))
evenNum = []
for Number in Numbers:
    if Number % 2 == 0:
        evenNum.append(Number)
print(sorted(evenNum, reverse=True))

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
rangeNumbers = list(range(1, 21))
for number in rangeNumbers:
    print(number)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

# rangeNumbers = list(range(0, 1000001))
# for number in rangeNumbers:
#    print(number)


# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
rangeNumbers = list(range(1, 1000001))
print(min(rangeNumbers))
print(max(rangeNumbers))
# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.
rangeNumbers = list(range(1, 21, 2))
for number in rangeNumbers:
    print(number)
# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
numbers = list(range(1, 11))
for number in numbers:
    thirdMultiple = number * 3
    print(thirdMultiple)
# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
numbers = list(range(1, 11))
for number in numbers:
    cubed = number ** 3
    print(cubed)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes

cubed = [number ** 3 for number in range(1, 11)]
print(cubed)

players = ['lis', 'thomas', 'gohar', 'sam', 'anand']
for player in players[1:4]:
    print(player.title())

# copy the list

myFood = ['pizza', 'burgers', 'subs', 'churros', 'nachos']
friendFood = myFood[:]
print("My favorite food are: ")
print(myFood)

print("My friends favorite are: ")
print(friendFood)
myFood.append('steak')
friendFood.append('lasagna')

print(myFood)
print(friendFood)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# •	 Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
# •	 Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
myFood = ['pizza', 'nachos', 'cake', 'cookies', 'tacos', 'sushi', 'eggs']
print("The first 3 items in the list are:")
print(myFood[:3])
print("\nThe 3 items from the middle of the list are:")
print(myFood[2:5])
print("\nThe last 3 items in the list are:")
print(myFood[4:])
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.
myfavPizzas = ["Cheese Pizza", "Jalapeno and Beef Pizza", "Barbaque Chicken"]
myFriendsPizzas = myfavPizzas[:]
myfavPizzas.append('Buffalo chicken pizza')
myFriendsPizzas.append('Pineapple pizza')

print("My favorite pizzas are: ")
for pizzas in myfavPizzas:
    print(pizzas)

print("My friends favorite pizzas are: ")
for pizzas in myFriendsPizzas:
    print(pizzas)

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
myFood = ['pizza', 'burgers', 'subs', 'churros', 'nachos']
friendFood = myFood[:]
myFood.append('steak')
friendFood.append('lasagna')
print("My favorite foods are: ")
for food in myFood:
    print(food)

print("My friends favorite foods are: ")
for food in friendFood:
    print(food)

# explanation of tuples

dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (100, 200, 300, 400)
print(dimensions)
for dimension in dimensions:
    print(dimension)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
print("\nMenu:")
buffet = ('chicken', 'burger', 'pizza', 'rice', 'noodles')
for food in buffet:
    print(food)
print("\nNew Menu:")
buffet = ('gumbo', 'steak', 'pizza', 'rice', 'noodles')
for food in buffet:
    print(food)