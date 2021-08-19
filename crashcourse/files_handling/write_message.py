filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# read mode 'r'
# write mode 'w'
# append mode 'a'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I love programming too.\n")
    file_object.write("I love creating new games too.\n")

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        guest = input("Enter a guest name: ")

        if (guest == ""):
            break

        file_object.write(guest + "\n")

filename = "reasons.txt"
with open(filename, 'w') as file_object:
    while True:
        res = input("Why do you like programming?")

        if (res == ""):
            break

        file_object.write(res + "\n")

