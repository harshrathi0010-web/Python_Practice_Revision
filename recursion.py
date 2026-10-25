"""

Recursion- It is a kind of property of a method where a method call itself...


def greet():
    print("hello")
    greet()

greet()


# WAP to sum of n number.
def add(num):
    if num==1:
        return 1
    else:
        return num+add(num-1)
print(add(12))

# WAP to cal the factorial of a number.
# hint-> 5 =5*4*3*2*1=120

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
print(fact(10))


"""





