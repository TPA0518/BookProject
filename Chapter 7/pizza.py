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