"""
# While loop

# It is also use to execute the same task again and again for the finite time.

syntax:
initializaiton
while condition:
        statement
        inc/dcr   # for breaking the loop

a=1
while a<5:
    print("hello")
    a+=1

# In while we can use the custom condition

a=1
while a<=5:
    name=input("Enter the name:")
    course=input("Enter the course name:")
    a+=1


# WAP to add the number
add=0
num=int(input("Enter the number for adding:"))
print("Number:",num)
while num>0:
    rem=num%10
    add=add+rem
    num=num//10

print("Sum of number:",add)


# WAP to reverse a number

add=0
num=int(input("Enter the number:"))
print("Number",num)
while num>0:
    rem=num%10
    add=add*10+rem
    num=num//10
print("Reverse number :",add)


# WAP to check num is armstrong.
# hint- 153--> 1**3 + 5**3 + 3**3=> 1+125+27  --> 153

num=int(input("Enter the number:"))
add=0
copy=num
print("Original number",num)
while num>0:
    rem=num%10
    add=add+rem**3
    num=num//10

print("Number after add",add)
if copy==add:
    print("Arm Strong")
else:
    print("Not arm strong")


"""
num=int(input("Enter the number:"))
add=0
copy=num
print("Original number",num)
while num>0:
    rem=num%10
    add=add+rem**3
    num=num//10

print("Number after add",add)
if copy==add:
    print("Arm Strong")
else:
    print("Not arm strong")
































