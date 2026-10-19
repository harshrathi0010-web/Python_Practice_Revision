"""
# LOOPS

a=50
for a in range(1,11,1):
    print("Yes")

for a in range(1,11,1):
    print("Yes")

for a in range(1,11,2):
    print(a)


for a in range(1,11):
    print(a)


for a in range(5):
    print(a)
# Output yes 50 times.

# WAP to counting num from 1-10
for a in range(1,11):
    print(a)

# WAP to print counting 1 to n
n=int(input("enter the number:"))
for a in range(1,n+1):
    print(a)

# WAP to find the factor of a number
# Hint- num-12  factor-1,2,3,4,6,12.

num=int(input("Enter the number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)

# WAP to count the factor of a number
# Hint- num-12  factor-1,2,3,4,6,12.
count=0
num=int(input("Enter the number:"))
for i in range(1,num+1):
    if num%i==0:
        
        count+=1
print("Total Factor",count)

# WAP to check if a num is prime or not.

count=0
num=int(input("enter the number:"))
for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print("Prime")
else:
    print("Not Prime")

"""















