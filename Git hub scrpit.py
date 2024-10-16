#this how to do a class to how different types of data for restrauent
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,number_served= 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(self.restaurant_name + ' ' + self.cuisine_type)
    
    def open_restaurant(self):
        print("Open")
    
    def set_number_served(self):
        print(self.number_served)
    
    def increment_number_served(self):
        self.number_served = self.number_served + 1
        print(self.number_served)

crpt = Restaurant("Craker Barrel", "Breakfest")
crpt.set_number_served()
crpt.describe_restaurant()
crpt.open_restaurant()
print(crpt.number_served)
crpt.number_served = 2
print(crpt.number_served)
crpt.increment_number_served()

deal = Restaurant("BurgerKing", "burgers")
deal.describe_restaurant()
deal.open_restaurant()
print(deal.number_served)
deal.number_served = 1
print(deal.number_served)
deal.increment_number_served()

obj1 = Restaurant("Arbys","beef")
obj1.describe_restaurant()
obj1.open_restaurant()
obj1.increment_number_served()

food = Restaurant("Subway","sandwitch")
food.describe_restaurant()
food.open_restaurant()
food.increment_number_served()

Place = Restaurant("Texas Roadhouse","steak")
Place.describe_restaurant()
Place.open_restaurant()
Place.increment_number_served()
#How a user is signing in how many times they have tried
class User:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name+ ' ' + self.last_name+ ' ' +self.age)

    def greet_user(self):
        print("Hello"+' '+self.first_name)
    
    def incrememt_login(self):
        self.login_attempts = self.login_attempts + 1
        print(self.login_attempts)
    
    def reset_login_attempts(self):
        self.login_attempts = self.login_attempts = 0
        print(self.login_attempts)
UserLaugh = User("Rick", "Oli", "36", 2)
UserLaugh.describe_user()
UserLaugh.greet_user()
UserLaugh.incrememt_login()
UserLaugh.reset_login_attempts()
class IceCreamStand(Restaurant):
    def __init__(self, flavors):
        self.flavors = flavors
    def display_flavor(self):
        print(self.flavors)

type = IceCreamStand(["Strawbarry","Oreo","Vanilla"])
type.display_flavor()
# this shows what pribileges a account has
class Admin(User):
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(self.privileges)

action = Admin(["can add post","can delete post","can ban user"])
action.show_privileges()
#this gives what privileges can be given
class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(self.privileges)

lost = Admin(["can add post","can delete post","can ban user"])
lost.show_privileges()
#this is how you get a random sequence of chracters
import random
Numbers = ['1','2','3','4','5','6','7','8','9','10','a','b','c','d','e']
a = []
a.insert(0,random.randrange(1,15))
a.insert(0,random.randrange(1,15))
a.insert(0,random.randrange(1,15))
a.insert(0,random.randrange(1,15))
print(a)
print("You win a prize")
#this is how you replace words with a different word
z = []
y = ''
file1 = open("learning_python.txt","r")
for x in file1:
    z.insert(0,x)
print(z[0])
print(z[1])
print(z[2])
y = z[0]
y = y.replace("in", "with")
print(y)
#how to set up die and roll it to get a random number
class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        print(random.randrange(1,6))
loop = Die()
loop.roll_die()
#how to plot fires in different areas and how dangerous they are
import matplotlib.pyplot as plt
import numpy as np

file = open("Fire.txt", 'r')
content = []
for line in file:
    content.insert(0,line)

o = []

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

print(o)

for u in content:
    o = u.split(",")
    print(o)
    ax.scatter(float(o[0]), float(o[1]), 0, 'z', float(o[2]))

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z label')
#how to plot numbers on a graph
w = []

for p in range(1,5000):
    w.insert(0,[p])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for r in w:
    ax.scatter(r, r, r)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show
#how to plot earthquakes
file2 = open("Coords.txt", 'r')
content1 = []
for line1 in file2:
    content1.insert(0,line1)

k = []

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

print(k)

for i in content1:
    k = i.split(",")
    print(i)
    ax.scatter(float(o[0]), float(o[1]), float(o[2]))

ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")