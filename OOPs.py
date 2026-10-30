"""

OOPS- object oriented programming

class,object
Encapsulation,polymorphism,Abstraction,inheritance

class ,object

Class: it is the virtual entity
class is a blueprint of an object
class is the representation of encapsulation.


syntax of class
class class-name:
        class's properties

class newClass():
    x=10
    def greet():
        print("Hello!")

print(x)  # here it will not work  bcoz class is virtaul


object : it is the real entity.
oject:is is the instance/outcome of a class

syntax:
    object_name=class_name()
    object_name.properties


class newClass:
    x=10
    def greet():
        print("Hello jiii")

obj=newClass
print(obj)
print(obj.x)  # here we can call x but x is stored in obj and obj is real

class newClass:
    x=10
    def greet():
        print("Hello jiii")

obj=newClass()
obj2=newClass()
print(obj)
print(obj2)
print(obj.x)           # if we change the object of one then it will not change oject of b

obj,x=2000
print(obj2.x)

print(obj.x)

# what is self
# self is the current class's object


def newClass():
    x=10
    def greet(self):
        print("value of x is",self.x)

    @staticmethod
    def welcome(self):
        print("welcome to my application")

obj=newClass  # we call the properites with help of object
obj.welcome()




# now here come dectorator to enhacne the functionaly of a func.


"""

# Constructor-->



















