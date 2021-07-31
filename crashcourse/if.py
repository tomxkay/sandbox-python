# if
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

# check whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# booolean expression
game_active = True
can_edit = False

# if conditional_test:
#   do something
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18")

age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")
if 'cheese' in requested_topping:
    print("Adding extra cheese")

print("\nFinished making your pizza")

alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points")
if alien_color == 'red':
    print("")

alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points")
else:
    print("You just earned 10 points")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + topping + ".")

print("\nFinished making your pizza")

# checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print("Adding " + topping + ".")
    else:
        print("Sorry, we don't have " + topping + ".")

print("\nFinished making your pizza!")

users = ['chris', 'dylan', 'tomx', 'admin']

if users:
    for user in users:
        if user == 'admin':
            print("Hello, admin")
        else:
            print("Hey " + user + " what's up!")

current_users = ['sally', 'gabby', 'dan', 'lex', 'tim']
new_users = ['sally', 'marco', 'tim', 'tom', 'carol']
for user in new_users:
    if user in current_users:
        print("Name is taken. You have to enter a username.")
    else:
        print("Username " + user + " is available.")

ordinal_numbers = range(1,10)
print(ordinal_numbers)
for number in ordinal_numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 2:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')







