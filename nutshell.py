# Data Types

type_str = "hello world"
type_int = 1
type_float = 3.14

type_str_multiline = """Some really big and long
                        text that spreads more than one
                        line but should still be readable
                        on a small terminal screen"""

## Falsey
type_none = None
type_true = True
type_false = False


# Data Structures
var1 = "hello world"
var2 = 42

str_list = ['bread', 'milk', 'cookies', 1, 2, 3]

print str_list[2]
del str_list[2]

str_list.append('rice')
print len(str_list)

## Immutable list
str_tupel = ('mooh', 3, 'test', 7)

## Dictionary: key-value-pairs unordered
phonebook = {
    'donald': 1234,
    'ronald': 4321,
    'sally': 6789
}

print phonebook['donald']
del phonebook['sally']
phonebook['pippi langstrumpf'] = 9876

## Set: dictionary consisting of only keys
str_set = set((1,2,3))

# Functions
print "hello sunshine"

## format strings
book = "neuromancer"
times = 2
print "I have read %s only %d times by now" % (book, times)

file = open("asset/test.txt")
file.close()

file = open("asset/test.txt")
print file.read()
file.close()

print range(23, 42)

## Custom function
def greet(name):
    print "Hello " + name

greet('Lucy')

def add(a=1, b=1):
    return a + b

print add(173, 91)


# Control Structures lstinlineif
a = "mooh"
if a == "mooh":
    print "Jippie"

a = []
if a: print "Hooray"

b = None
if b: print "Donald has luck"

c = ""
if c: print "I love rain"

list = [range(10)]
print list

if len(list) < 0:
    print ":("
elif len(list) > 0 and len(list) < 10:
    print ":)"
else:
    print ":D"

books = (
    'the art of deception',
    'spiderman',
    'firestarter'
)

## Loops
for book in books:
    print book

for line in open("asset/test.txt"):
    print line

x = 1
while x < 10:
    print "%s" % x
    x = x + 1


# Modules
# import sys
# print sys.version
# sys.exit(1)

# from sys import exit
# exit(1)


# Exceptions
try:
    fh = open("somefile", "r")
except IOError:
    print "Cannot read somefile"


# Regular Expression


# Sockets



