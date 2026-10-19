"""

Tuple-> Tuple is also a collection like list which can hold
hetergenous (different) data type elements


t1=(10,304,55,204)
print(t1)
print(type(t1))


t1=(10,20,"A",True,3+8j)
print(t1)

# Tuple work on index (forward,backward)

t=(34,5,4,7,55,78)
print(t)
print(t[1])  # pass index num here!
print(t[-5])

# Tuple also support slicing
print(t[2:5])
print(t[-5:-9])

# Tuple also support replication
print(t*3)

# Tuple can be replicate or Iterate
print(t)
for i in t:
    print(i)

# Tuple can work with build in functions
print(sum(t))
print(min(t))

# Tuple Method-- Only Count,Index.

t=(10,30,403,22,99)
print(t)
print(t.count(10))
print(t.index(22))

# Tuple is immutable you can't change anything in the tuple
# and list is mutable (change possible)


# Tuple is a static memory we can make it dynamic memory
# Interview ques
# here we make a mutable oject inside immutable object nd we can change it
t=(10,20,405,[2,43,5,7],4,67)
t2=(10,20,405,[2,43,5,7],4,67)
t[3].append(99)

print(t)


t3=(10,20,30,40)
t4=(10,20,30,40)
print(t3 is t4)



# STRING - It is also a collection of character and it behaves like a tuple
# Syntax-
st="harsh rathi"
print(st)
print(type(st))
st="harsh"
print(st)

st1=str(123)
print(st1)


st="Harsh Rathi"
print(st)
print(st[2:7])

# String also support replication.
print(st*3)

# String can be traverse
for s in st:
    print(s)



# string can also support build in functions.
st="aman kumar"
print(len(st))
print(max(st))
print(min(st))


# Char are the char value of the some numeric value
# which is ASCII valies
# A=65,B=66,Z=90
# a=97,b=98,c=99,z=122

a=65
print(a)
print(chr(a))

a="z"
print(ord(a))


#String has some methods like lower,upper,title,strip,split,replace.
st="Harsh RAThi  "
print(st)
print(st.lower())
print(st.upper())
print(st.title())
print(st.strip())

st2="Aman is my younger brother"
li=st2.split()
print(li)

st="    aman   "
print(st.strip()) # return a new string after removing white spaces
print(st)

st="    aman   "
print(st.strip()) # return a new string after removing white spaces
print(st)



"""









































