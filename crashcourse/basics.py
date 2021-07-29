# Variables
message = "Hello Python World!"
print(message)
message = "Hello Python Crash Course World!"
print(message)

# variable names can contain letters, numbers, underscores
# variable names should be short but descriptive

# strings
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# concatenating strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())

# adding whitespace to strings with tabs or newlines
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping whitespace
favorite_language = " python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

quoter = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new"
print(quote + " - " + quoter);

# numbers
# integers
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)

# floats
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 + 0.2)

print(0.2 + 0.1)

age=23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

favorite_number = 1
message = "My favorite number is " + str(favorite_number)
print(message)

# comments
