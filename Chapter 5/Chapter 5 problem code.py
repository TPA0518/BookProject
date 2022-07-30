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

bannedUsers = ['andrew', 'ahmed', 'david']
user = 'thomas'
if user not in bannedUsers:
    print(user.title() + ' is not a banned user.')

print(" Is user == thomas? I predict True.")
print(user == 'thomas')

print(" Is user == bob? I predict False.")
print(user == "bob")

