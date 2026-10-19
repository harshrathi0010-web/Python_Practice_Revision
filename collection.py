

"""
Collection-It is a group of elements in a single unit

-Sequence data type- List,Tuple,String
-Hash Data Type-Set ,dict

List-Collection of hetregenous (different) data type elements.
Syntax-
li=[3,44,53,5,543]
li=[3,44,53,5,543]
li1=[23,5.2,"A",True,4+8j]
li=[]
li=list([34,43,10])
li=list((10,20,30))
li=list()
print(li)
print(type(li))

# List work with index(forward and backward)
# There is no fixed memory in elements of list
#  Forward Index work from here 0,1,2,3,4
# Backward index work from -1,-2,-3 and -4
# List can be sliced

li=[10,203,450,5,12]
print(li)
print(li[2])
print(li[-3])
print(li[1:4])  # for printing mutiple values
print(li[:4])
print(li[:])
print(li[-4:-1])
print(li[-3:-7]) # will print null
print(li[-3:-7:-1])


li1=[10,20,30]
print(li1)
print(li1*3)  # List can be replicate.

# List can be traverse/Iterate

li=[10,20,30,40,50]
print(li)
for x in li:
    print(x)
    print(x**3)
     can be work with build in function.

     
# sum,max,min,len
# list has some methods-append,extend,insert

li=[10,20,44,6,45]
print(sum(li))
print(max(li))
print(len(li))

print(sum(li)/len(li))  # for avg

li.append(99)
print(li)

li.insert(3,100)
print(li)

li2=[11,2,33,455]
li.extend(li2)
print(li2)
print(li)



# POP,remove,clear,del(keyword)
li=[10,343,54,367,36]
print(li)
li.pop()
print(li)
li.pop(1)
print(li)# Remove by index
li.remove(54)
print(li)

del li[1]  # KEyword not a word of list
print(li)

li.clear()
print(li)

li=[10,4,3,636,63,35]
print(li)
li.reverse()
print(li)

li.sort()
print(li)

# count,index
li=[10,204,10,5,6,4,3]
print(li.count(10))
print(li.index(10))
print(li.index(4))


"""

















    















































