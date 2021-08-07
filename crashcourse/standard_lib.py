# the python standard library is a set of modules included with every python
# installation

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")



from random import randint
x = randint(1, 6)

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        print(randint(1,self.sides))

    def set_sides(self,sides):
        self.sides = sides


die = Die()
for i in range(0, 10):
    die.roll_die()

die.set_sides(10)
for i in range(0, 10):
    die.roll_die()

die.set_sides(20)
for i in range(0, 10):
    die.roll_die()
