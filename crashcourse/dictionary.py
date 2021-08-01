# dictionary: a collection of key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# accessing values in a dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0= {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

# removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
person = {
    'name': 'thomas kay',
    'age': 28,
    'profession': 'coder',
    'location': 'tulsa, ok'
}
print("Person name is " + person['name'])
print("Person age is " + str(person['age']))
print("Person profession is " + person['profession'])
print("Person location is " + person['location'])

# looping though all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

print(user_0)

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for k, v in user_0.items():
    print("\nKey: " + k)
    print("Value: " + v)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite lanugage is " + language.title())

# looping though all keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")

# looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


for language in set(favorite_languages.values()):
    print(language.title())

country_rivers = {
    'nile': 'egypt',
    'mekhong': 'vietnam',
    'saluda': 'usa',
}

for river in country_rivers:
    print river.title();

for country in country_rivers.values():
    print country.title();

# nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

# a list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

users = {
    'aeinsteinn': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

pets = {
    'queso': {
        'kind': 'cat',
        'owner': 'tomx',
    },
    'nuique': {
        'kind': 'cat',
        'owner': 'tomx',
    },
    'echo': {
        'kind': 'gecko',
        'owner': 'tomx',
    },
}

for name, info in pets.items():
    print(name + " is a " + info['kind'] + " and belongs to " + info['owner'])

