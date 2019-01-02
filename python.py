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

