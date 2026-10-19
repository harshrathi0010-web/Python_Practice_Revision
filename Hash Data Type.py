"""
Hash Data Type-Set,Dict


Set- It is a collection of hetregenous(different) it is collection of unique values
Set - It does not preserve the order of elements .data will be shuffled
set-It automatically remove duplicates values
set has no index.
set can not be sliced.
set cannot be replicate.
set can be traverse


set1={45,52,"ab",3+8j}
set2={456,1,2,79,2,2,2,76}
set3={}
print(set1)
print(set2)  # did not contain duplicate value
print(set3)
for a in set2 :
    print(a)
print(type(set1))

print(sum(set2))
print(len(set2))

# Set has its own methods-> add,pop,remove,discard.
s={10,2,35,78,98,99}
print(s)
s.pop()  # Completely random
print(s)
s.add(100) # Completely random
print(s)
s.add(44)
print(s)
s.remove(99)   # static
print(s)
s.discard(2)  # remove value from the set
print(s)

s.clear()
print(s)

# Intersection,union,difference,symatic differnce
s1={10,2,3,4,78,43,43,99}
s2={45,5,99,90,12,34}
print(s1.intersection(s2))  # Common values

print(s1.union(s2)) # combine both and remove duplicates

print(s1.difference(s2)) # s1-s2 , remove common elements

print(s1.symmetric_difference(s2))


# Set operator's

s1={1,2,4,5,6}
s2={4,5,6,7,8}
print(s1&s2)  # Intesection
print(s1|s2) # union
print(s1-s2)#diff
print(s1^s2)# symmetric_diff





Dictionary-it is collection of key value pairs and key value pairs called items.
Dict do not work witht the index
it work with the keys
Dict- it can store duplicates values but cannot duplicates key
dict can not be sliced,Replicated but dict can be traverse


d={1:267,2:455,3:267,"Aman":100}  
print(d)
print(type(d))
print(d[1])# index work like 1,2,3
print(d[3])
print(d[2])
print(d[4])


d={1:267,2:455,3:2067,"Aman":100,15:"Harsh"}
print(d.items())

for i in d.items():
    print(i)

# update,POP,
d={1:23,2:90,3:22,4:65}
print(d)
d[2]=999
print(d)
d2={4:666,5:88,6:444,7:999}
d.update(d2)
print(d)
d.pop(4)
print(d)
d.popitem()
print(d)


"""




    

    






































