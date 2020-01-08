import  random
import sys
import  os
"""
It's a comment block

"""

#It's a single line comment
print("Hello World")

name = "Jakub"
print(name)
name = 15
print(name)
print(5//2)
print(5**3)
quote = "\"Always remember you are uniqie"

multi_line_quote = ''' just
    line everyone else'''

print("%s %s %s" %('I like the quote', quote, multi_line_quote))

print("I don't like ", end="")
print("newlines")

list = ['Juice', 'Tomatoes', 'Potatoes']
print("First Item", list[0])
list[0] = "Cucumbers"
print(list[0:3])

list.append('Apples')
print(list[0:4])
list.remove('Potatoes')
print(list[0:4])
list.sort()
print(list[0:4])
del list[2]
cars = ['Ferrari', 'Lamborghini', 'Honda', 'Ford', 'Toyota']
planes = ['Cirrus', 'Honda', 'LearJet']

vehicles = cars + planes
print(vehicles)
print(min(vehicles))
print(max(vehicles))
vehicles.sort()
print(vehicles)



tuple = (3,1,4,3,32,45,43)
print(tuple)




dictionary ={'Fiddler' : 'Isac Bowin' , 'Capitan Cold' : 'Leonard Snart'}
print(dictionary['Fiddler'])
dictionary['Fiddler'] = 'Hartley'
print(len(dictionary))
print(dictionary)
print(dictionary.values())

age = 21

if age == 18 :
    print("You are old enough to drive")
else :
    print("You are not old enough to drive")

height = 150
if height > 180 :
    print("You are tall ")
elif ((height > 170) and not(age > 18)):
    print("You are young and tall")
else :
    print("You are medium height")


for x in range(0,10):
    print(x, ' ',end='')

print()#new line

for x in list:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in num_list:
    print(x)

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])


random_num = random.randrange(0,20)
while(random_num !=0):
    print(random_num)
    random_num = random.randrange(0,20)

i = 0

while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i+=1
        continue
    i+=1

def addNumber(fNum,lNum):
    sumNum = fNum + lNum
    return sumNum


print((addNumber(1,2)))

print("What is your name?")

name = sys.stdin.readline()

print("Hello", name)

long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])
print(long_string[-6:])
print(long_string[:-6])

print(long_string[:4] + " be there")


print("%c is my %s letter and my %d number is %.5f" %('X', 'favourite', 1, 0.40))


print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Floor", "Ground"))
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)

file = open("text.txt", "wb")
print(file.mode)
print(file.name)
file.write(bytes("Write to file\n",'UTF-8'))
file.close()
file = open("text.in","r+")
text_in_file = file.read()
print(text_in_file)

os.remove("text.in")

#Objects

class Animal:
    #Local variables
    __name = None
    __height = None
    __weight = None
    __sound = None
    
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    
    def set_name(self, name):
        self.__name = name
    
    def set_height(self, height):
        self.__height = height
    
    def set_weight(self, height):
        self.__height = height
    
    def set_sound(self, sound):
        self.__sound = sound
    
    def get_name(self):
        return self.__name
    
    def get_height(self):
        return str(self.__height)
    
    def get_weight(self):
        return str(self.__weight)
    
    def get_sound(self):
        return self.__sound
    
    def get_type(self):
        print("Animal")
    
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name, self.__height, self.__weight, self.__sound)



cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())


class Dog(Animal):
    __owner = None
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)
    
    def set_owner(self, owner):
        self.__owner = owner
    
    def get_owner(self):
        return self.__owner
    
    def get_type(self):
        print ("Dog")
    
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)




spot = Dog("Spot", 52, 27, "Ruff", "Bob")
print(spot.toString())



"yahoo!" if 3 > 2 else 2  # => "yahoo!"
li = []
li.append(1)
li.append(2)
li.append(4)
li.append(3)
li.pop()        # => 3 and li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3] again.
# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3
# Looking out of bounds is an IndexError
li[4]  # Raises an IndexError

li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting every second entry => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]

del li[2]  # li is now [1, 2, 3]

# Check for existence in a list with "in"
1 in li  # => True



# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

filled_dict["one"]  # => 1
list(filled_dict.keys())  # => ["one", "two", "three"]
list(filled_dict.values())  # => [1, 2, 3]

"one" in filled_dict  # => True
1 in filled_dict      # => False

filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict



list = ["dog", "cat", "mouse"]
for i, value in enumerate(list):
    print(i, value)
#  =>
#0 dog
#1 cat
#2 mouse


# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")



# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)




# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}


# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
    
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
