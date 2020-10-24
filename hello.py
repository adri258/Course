"""
print("Hello world" )


name = input("Name: ")
print("Hello,"+ name)
print(f"Hello, {name}")

n = int(input("Number: "))
if n>0:
    print(f"{n}, is possitive")
elif n <0:
    print(f"{n}, is negative")
else:
    print(f"{n}, is zero")
"""
"""
#Define list of names
name = ["Adriana", "Martin", "Tatusko"]
print(name)

name.append("Mamicka")
name.sort()
print(name)

#list = sequence of mutable values
#tuple = sequence of immutable values
#set = collection of key-value pairs
#dic = collection of key-value pairs
"""

"""
#create an empty set
s = set()
#add elements
s.add(1)
s.add(2)
s.add(3)
s.add(2)
s.add(3)
s.remove(2)
print(s)

print(f"The set has {len(s)} elemnts.")
"""

"""
#loops
#for i in [0,1,2,3,4]:
#    print(i)

#for i in range(6):
#    print(i)

#names = ["Adka", "Matko", "Lubosko", "Daska"]

#for name in names:
#    print(name)

names = "Harry"
for character in names:
    print(character)
"""

#dictionaries
"""
houses = {"Adka": "Innovatrics", "Luki": "Powerfull medical"}

houses["Natalka"] = "Decathlon"
print(houses["Natalka"])
"""
#from functions import square

#for i in range(10):
#    print(f"The square of {i} is {square(i)}")
"""
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
"""

#classes
"""
class Point(object):
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2

p = Point(2,3)
print(p.x)
print(p.y)#
"""
"""
class Flight():
    def __init__(self, capacity): #create new flight
        self.capacity = capacity
        self.passangers = []

    def add_passenger(self, name):#add passangers to flight
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passangers)

flight = Flight(3) #define max number of available seats for Flight
people = ["Adka", "Matko", "Misko", "Luki"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
"""
