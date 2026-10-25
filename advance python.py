""""
Advance python - lambda,map,reduce,apply,filter
lambda-> It is a keyword use to write short defination methods.




def cube(num):
    return num**3

print(cube(4))


# here instead of this  we can write the lambda function which is short.

cube=lambda num:num**3
print(cube(10))


square=lambda num:num**2
print(square(4))


# WAP to check num is even or odd

def check_Even(num):
    if num%2==0:
        return 'Even'
    else:
        return 'odd'

print(check_Even(6))
print(check_Even(9))

# with help of lambda
check_even=lambda num:  "even" if num%2==0  else "odd"
print(check_even(15))


# we have to print the square of these list num.

li=[5,10,20,45,6]
square=lambda num:num**2
for i in  li:
    print(square(i))

# here we did not have to work like this
# here come map function

map-> map is a built in function used to apply a method on a collection
without iteration.

square=lambda val:val**2
li=[10,20,4,33]
res=list(map(square,li))
print(res)

Filter-> Filter is built in function in python which is use to apply a method
on a collection without iteration but your method should return boolean ans/result
and the method will filter elements from the collection.



check_even=lambda num: True if num%2==0 else False
li=[x for x in range(1,11)]  # list comprehension
res=list(filter(check_even,li))
print(res)


add=lambda a,b:a+b
li=[x for x in range(1,31) if x%3==0] # List comprehnesion

res=0
for x  in li:
    res+=x
print(res)



# Reduce-> it is method use to calculate a value using a collection without iteration.
from functools import reduce 
add=lambda a,b:a+b
li=[x for x in range(1,31) if x%3==0]
res=reduce(add,li)
print(res)



# WAP To calc the sum of all even square of a collection.

from functools import reduce 
check_even=lambda num:  num%2==0
square=lambda num:num**2
add=lambda a,b:a+b
li=[1,2,3,4,5,68,8]

even=filter(check_even,li)
sq=list(map(square,even))
res=reduce(add,sq)
print(res)



"""





    





































