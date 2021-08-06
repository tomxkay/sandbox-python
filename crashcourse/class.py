# classes are used to model the real world by storing the function, features
# and characteristics that makes up the real world item

# classes represent real-world things and situations
# objects are instances of classes

# instantiation
# instance


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# method
# attribute

my_dog = Dog("willie", 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# access attributes
# dot notation

# calling methods
my_dog.sit()
my_dog.roll_over()

# creating multiple instances
my_dog = Dog("willie", 3)
your_dog = Dog("max", 4)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            "The "
            + self.name
            + " restaruant serves "
            + self.cuisine_type
            + " cuisine!"
        )

    def open_restaurant(self):
        print("The " + self.name + " restarnt is now open")


restaurant = Restaurant("ice cold boba", "drinks")
print("The restaurant name is " + restaurant.name.title() + ".")
print("The restaurant serves " + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("chik-fil-a", "chicken")
restaurant3 = Restaurant("taco bell", "tacos")

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first, last, **user_info):
        self.first = first
        self.last = last
        self.user_info = user_info

    def describe_user(self):
        print("First name: " + self.first)
        print("Last name: " + self.last)

        for k, v in self.user_info.items():
            print(k + ": " + v)

    def greet_user(self):
        print("Hello " + self.first + " " + self.last)


user1 = User("thomas", "kay", age="28", occupation="coder")
user1.describe_user()
user1.greet_user()

user2 = User("carol", "kay", age="21", occupation="boss")
user2.describe_user()
user2.greet_user()


# working with classes and instances
# you can use classes to represent many real-world situations
# setting a default value for an attribute
# modifying an attribute's value through a method


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_used_car = Car("subaru", "outback", 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            "The "
            + self.name
            + " restaruant serves "
            + self.cuisine_type
            + " cuisine!"
        )

    def open_restaurant(self):
        print("The " + self.name + " restarnt is now open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant("pizza world", "pizza")
print(restaurant.number_served)
restaurant.number_served = 4
print(restaurant.number_served)
restaurant.set_number_served(50)
print(restaurant.number_served)
restaurant.increment_number_served(50)
print(restaurant.number_served)


# inheritance
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't needa gas tank")


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


# instances as attributues


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't needa gas tank")


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()


# modeling real-world objects
# think at a higher logical level rather than a syntax-focused level
# there are often no right or wrong approaches to modeling real-world situations
# some approaches are more efficient than other, but it takes practice to find
# the most efficient representations.

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolate']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

icecream_stand = IceCreamStand('my_icecream_stand', 'icecream')
icecream_stand.display_flavors()

class Admin(User):
    def __init__(self, first, last, **user_info):
        super().__init__(first, last, **user_info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def display_priviledges(self):
        for privilege in self.privileges:
            print(privilege)

sys_ad = Admin('thomas', 'kay', age="28", occupation="coder")
sys_ad.display_priviledges()

class Admin(User):
    def __init__(self, first, last, **user_info):
        super().__init__(first, last, **user_info)
        self.privileges = Priviledges()

class Priviledges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def display_priviledges(self):
        for privilege in self.privileges:
            print(privilege)

sys_ad = Admin('thomas', 'kay', age="28", occupation="coder")
sys_ad.privileges.display_priviledges()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't needa gas tank")

    def upgrade_battery(self):
        if self.battery.battery_size != 85:
            self.battery.battery_size = 85


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.upgrade_battery()
my_tesla.battery.get_range()


