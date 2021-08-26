import json

numbers = [2,3,5,7,11,13]

filename = 'test.txt'
with open(filename) as f_obj:
    test = json.load(f_obj)

# refactoring makes your code cleaner, easier to understand, and easier to
# extend.


