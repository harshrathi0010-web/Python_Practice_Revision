"""
*****
*****
*****
*****
*****


for i in range(1,7):
    for j in range(1,7):
        print("*",end='')
    print()
    

*
**
***
****
*****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()

1
12
123
1234
12345

for i in range(1,6):
    for j in range(1,1+i):
        print(j,end='')
    print()

1
22
333
4444
55555

for i in range(1,6):
    for j in range(1,1+i):
        print(i,end='')
    print()

1
23
456
78910

k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end='')
        k+=1
    print()


A
AB
ABC
ABCD
ABCDE

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()

A
BC
DEF
GHIJ
KLMNO


k=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end="")
        k+=1
    print()


    *
   **
  ***
 ****
*****

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

    *
   * *
  * * *
 * * * *
* * * * *

for i in range(1,6):
    for k in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()

0
909
89098
7890987
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321

st="0"
for i in range(10,0,-1):
    if i!=0:
        st=str(i) + st + str(i)
    print(st)


"""



    
        














    
        













 
