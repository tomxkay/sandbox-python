# list: a collection of items in a particular order
bicycles = ['treak', 'cannnondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# adding to the list
motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'tesla')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# removing from the list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

guests = ['michael kay', 'tina ka', 'tiffany ka']
print("Guests invited to dinner " + str(guests))

sister = 'tina ka'
guests.remove(sister)
print(sister + " couldn't make it to dinner")

guests.insert(1, 'grace ka')
print("Guests invited to dinner " + str(guests))

uncle = "dylan tran"
print("Found another guest to join dinner: " + uncle)
guests.insert(0, uncle)
print("Guests invited to dinner " + str(guests))

aunt = "nicole cil"
print("Found another guest to join dinner: " + aunt)
guests.insert(len(guests)/2, aunt)
print("Guests invited to dinner " + str(guests))

grandma = "nga tran"
print("Found another guest to join dinner: " + grandma)
guests.append(grandma)
print("Guests invited to dinner " + str(guests))

uninvited = guests.pop();
print("Sorry " + uninvited + " you're uninvited.")

uninvited = guests.pop();
print("Sorry " + uninvited + " you're uninvited.")

uninvited = guests.pop();
print("Sorry " + uninvited + " you're uninvited.")

uninvited = guests.pop();
print("Sorry " + uninvited + " you're uninvited.")

print(guests)

print(guests[0].title() + " you're still invited.")
print(guests[1].title() + " you're still invited.")

# organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)
print(len(cars))

places = ['new york', 'isreal', 'vietnam', 'alaska', 'hawaii']
print(places)
places.sort()
print(places)

places = ['new york', 'isreal', 'vietnam', 'alaska', 'hawaii']
print sorted(places)
print(places)
places.reverse()
print(places)

# working with lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show")


pizzas = ['pepperoni', 'cheese', 'bacon']
for pizza in pizzas:
    print("I love " + pizza + " pizza!")

print("I love all pizzas")

animals = ['gecko', 'lizard', 'tortoise']

for animal in animals:
    print("A " + animal + " would make a greak pet")
print("Any of these animals would make a great pet")

# ranges
for value in range(1,5):
    print(value)

# use range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

digits = [1,2,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))

# list comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

for number in range(1,21):
    print(number)

# numbers = range(1, 1000001)
# print min(numbers)
# print max(numbers)
# print sum(numbers)

odd_numbers = range(1,21,2)
print(odd_numbers)

multiple_of_threes = []
for number in range(3,31,3):
    print(number)

cubed = []
for number in range(1,11):
    cubed.append(number**3)
print(cubed)

cubed = [number**3 for number in range(1,11)]
print(cubed)

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:])
print(players)

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

print("The first three items in the list are: ")
print(my_foods[:3])
print("The items from the middle list are: ")
print(my_foods[(len(my_foods)/2) - 2:(len(my_foods)/2) + 1])
print("The last three items in the list are: ")
print(my_foods[-3:])

pizzas = ['pepperoni', 'cheese', 'bacon']
friend_pizzas = pizzas[:]
friend_pizzas.append('chicken')
print("My favoriate pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("My friend's favoriate pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)

# tuples: immutable list
# a tuble is like a list but uses parentheses instead of square brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)


