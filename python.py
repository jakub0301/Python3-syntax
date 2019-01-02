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


