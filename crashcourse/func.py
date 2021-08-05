# functions: named blocks of code that are designed to do one specific job
def greet_user():
    print("Hello!")


greet_user()


def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user("jesse")


def display_message():
    print("I learning the core fundamental of python from this book")


display_message()


def favorite_book(title):
    print("One of my favorite books is " + title.title())


favorite_book("anna karenia")

# positional arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("cat", "queso")
describe_pet("cat", "nuique nuique nuique")

# keyword arguments
describe_pet(animal_type="cat", pet_name="queso")

# default value
# any parameter with a default value needs to be listed after all the parameters
# that don't have default values


def make_shirt(size, message):
    print(
        "The shirt is a size "
        + str(size)
        + " with a message of "
        + message
        + " printed on it"
    )


make_shirt(5, "yolo")
make_shirt(message="yolo", size=5)


def make_shirt(message="I love python", size="large"):
    print(
        "The shirt is a size "
        + str(size)
        + " with a message of "
        + message
        + " printed on it"
    )


make_shirt(size="large")
make_shirt(size="medium")
make_shirt(size="small", message="python is not bad")

# return values


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)

# making an argument optional
# returning a dictionary


def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    return person


person = build_person("thomas", "kay")
print(person)


# using a function with a while loop

# passing a list
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

# modify a list in a function
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for model in completed_models:
    print(model)


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)


unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# preventing a function from modifying a list
magicians = ["copperfield", "penn", "teller"]


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


show_magicians(magicians)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"
        return magicians


make_great(magicians)
show_magicians(magicians)

magicians = ["copperfield", "penn", "teller"]
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
show_magicians(magicians)

# passing an arbitrary name of arguments
def make_pizza(*toppings):
    print("\nMaking apizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


def make_pizza(size, *toppings):
    print(
        "\nMaking a " + str(size) + "-inch pizza with the following toppings:"
    )
    for topping in toppings:
        print("- " + topping)


make_pizza(12, "pepperoni")
make_pizza(6, "mushrooms", "green peppers", "extra cheese")


def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last

    for key, value in user_info.items():
        profile[key] = value

        return profile


# the double asterisks before the parameter **user_info tells python to create
# an empty dictionary called user_info and pack whatever name-value pairs it
# receives into this dictionary
user_profile = build_profile(
    "albert", "eistein", location="princeton", field="physics"
)

print(user_profile)

# you can mix positional, keyword, arbitrary values in many different ways when
# writing your own functions

# remember to use the simplest approach that gets the job done and progress to
# more efficient approaches each time.


def make_sandwich(*items):
    print("This sandwich contains:")
    for item in items:
        print("- " + item)


make_sandwich("lettuce", "cheese", "ham")
make_sandwich("cheese", "turkey", "beef", "ketchup")
make_sandwich("avacado", "lettuce")


def build_profile(first, last, **user_info):
    profile = {
        "first_name": first,
        "last_name": last,
    }
    for k, v in user_info.items():
        profile[k] = v

    return profile


my_profile = build_profile("thomas", "kay", age=28, job="coder")
print(my_profile)

def make_car(manufacturer, model, **features):
    car = {
        "manufacturer": manufacturer,
        "model": model,
    }

    for k,v in features.items():
        car[k] = v

    return car

car = make_car('toyota', 'camary', color="silver", year="2016")
print(car)

