"""

UDF:User define function
A function written by user can be reused and also dump as the method.

syntax-

def function_name(paramter):
                defination

def greet():  # Proto type
    print("Good Morning")

greet()  # calling

greet()
print("Hello")
greet()

A function is a block of statements that perform a
specific task
and return a value.


def greet(var):
    print("Good",var)

greet("Morning")
greet("Afternoon")

 # Now the code is dynamic.



def greet(var):
    return "Good "+var

print(greet("Morning"))
print(greet("Noon"))

# WAP to add two number

def add(a,b):
    return a+b

print(add(10,20))
print(add(2,7))


 WAP to add multiple number.

def add(a,b,c=0,d=0):
    return a+b+c+d

print(add(20,43,53,99))

# now if we pass only here three values

print(add(20,1,2)) # It will give the error
                  # so here we make c nd d variable.


#
def add(*a):   # args=> tuple
    print(type(a))
    return sum(a)

print(add(34))
print(add(34,100))
print(add(34,5,12))  
print(add(34,5,12,4444)) 


def info(**data):     # now it is dict
    return data

print(info(name="Raman Singh",salary=43234))



# WAP to check a num is prime or not.

def checkprime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return("Prime Number")
    else:
        return("Not Prime")
n=int(input("enter the number:"))
print(checkprime(n))

# wAP to print all prime b/w 1-100

def checkprime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count==2

for i in range(1,101):
    if checkprime(i):
        print(i)
        
"""


















 















