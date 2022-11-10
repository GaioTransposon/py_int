from re import X
import numpy as np


def print_test():
    print("test")


def print_test2():
    print("test", "bye")


print_test2()






# Making a function that takes any number of arguments:
def addition(*args):
    result = 0
    for n in args:
        result = result + n
    return result


a = addition(2, 3, 4)
print(a)

def min2(*args):

    my_min = args[0]

    for i in args:

        if i == my_min:
            print("nope1")

        elif i < my_min:
            my_min = i

        else:
            print("nope2")

    return my_min


ans = min2(10, 3, 4, -2, 5)
print(ans)


###############################
# Object-oriented programming:

# Objects - classes:
import math

# Base class
class Shape:
    def area(self):
        print("I don't know who I am therefore don't know my area")

    def circumference(self):
        print("I don't know who I am therefore don't know my circumference")

class Position():
    def __init__(self,x,y):
    self.x=x
    self.y=y

# Derived class from shape
class Circle(Shape):
    radius = 0
    position = Position(0,0)

    def __init__(self, radius, color="White"):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius**2


my_circle = Circle(2.0, "Red")
print(my_circle.color)

my_circle2 = Circle(2.0)
print(my_circle2.color)

print(my_circle.area())



circles=[]
for n in range(10):
    circles.append(Circle(n+1))

    full_area=0

    for circle in circles:
        full_area+= circle.area()


###############################

def noise(animal):
    if (isinstance(animal, Cat)):
        print("Meow")

class Animal():
    def __init__(self, weight):
        self.weight = weight


    def noise(self):
        print("???")

class Cat(Animal):
    pass


my_cat = Cat(12.0)
my_cat.
my_cat.noise()
noise(Cat(12.0))

animals = { "Cat" : {"Weight": 12.0, "Noise": "Meow" }}

###############################


class Complex():

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return Complex(new_real, new_imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"



c1 = Complex(4, 3)
c2 = Complex(-1, -7)

print(c1.__add__(c2))
print(c1+ c2)
# c1.__add__(c2)

###############################


import math

# Base class
class Shape():
    def area(self):
        print("I don't know how I look like so I don't know my area")
    def circumference(self):
        print("I don't know how I look like so I don't know my circumference")


class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Derived class from Shape
class Circle(Shape):
    radius = 0
    position = Position(0, 0)

    def __init__(self, radius, color = "White"):
        self.radius = radius
        self.color = color


    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


my_circle = Circle(1.0)
print(my_circle.color)

my_circle2 = Circle(2.0, "Red")
print(my_circle2.color)

circles = []
for n in range(10):
    circles.append(Circle(n + 1))

full_area = 0

for circle in circles:
    full_area += circle.area()

print(f"Area of all circles {full_area}")


shapes = [Circle(1.2), Rectangle(2,3)]

full_area = 0
for shape in shapes:
    full_area += shape.area()


