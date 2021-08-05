# user input and while loops
# most programs are written to solve an en user's problem

# the input() function pauses your program and waits for the user to enter some text.
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message);

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# modulo operator: divides one number by another number and returns the remainder
print(4 % 3)
print(5 % 3)
print(6 % 3)

# while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# break
# continue

# using a while loop with lists and dictionaries
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# filling a dictionary with user input


