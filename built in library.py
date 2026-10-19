"""
print("Hello")
Built in functions-print,num,int,float etc

Build in libraries

import library_name
from library_name import fun1,fun 2


import math
print(math.sqrt(125))
print(math.pi)
print(math.factorial(6))


from math import factorial,sqrt
print(sqrt(625))
print(factorial(6))



# RANDOM
import random
print(random.random())# will print random value b/w the 0 and 1.
print(random.random()*10)
print(random.random()*100)

from random import randint
print(randint(1,8)) # here it will print random num between the 1,8
print(randint(1000,9999)) # want to generate OTP numbers


# WAP to program or a small guessing game number.
import random
num=random.randint(1,10)


a=1
while a<=4:
    ch=int(input("Guess number between 0 and 10:"))
    if num==ch:
        print("You winn")
    else:
        print("Loss")
        a+=1

"""

# ATM simluation COde

































