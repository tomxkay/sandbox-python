with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

for content in contents:
	print(content.rstrip())

	pi_string = ''
	for line in contents:
		pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# when python reads from a text file, it interprets all text in the file as a
# string

# python  has no inherent limit to how much data you can work with; you can work
# with as much data as your system's memory can handle

with open('learning_python.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

for content in contents:
	print(content.rstrip())


learned = ''
for content in contents:
	learned += content.rstrip()

print(learned)

with open('learning_python.txt') as file_object:
	lines = file_object.read()
	print(lines.replace('python', 'C#'))
