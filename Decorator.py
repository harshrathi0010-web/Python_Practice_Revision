"""

Decorator--> it is property of method which will enhance the works or defination of a method




def greet():
    print("hello")

greet()- > method
greet -> method execution


def my_decorator(func):
    def wrapper():
        print("Program started")
        func()
        print("ended")
    return wrapper

@my_decorator
def greet():
    print("hello")

@my_decorator
def closing():
    print("Good night")

@my_decorator
def greet():
    print("hello")
greet()

closing()


"""





   


