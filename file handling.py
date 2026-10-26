"""
File handling-It is used to handle a file to read or write data from a text/binary.

1.text file-- .txt,.pdf,.xlsx,.csv
    text file store data char by char and binary files stores data object by oject.


2.binary file-- (.dat,.bin etc)


Text file
file_handler=open("filename.extension","mode")
model:reason of opening - r,w,a,r+,w+,a=

file=open("student.txt","w")

# if mode is write or append then will be automatically created if does not exist.
# if exist mode was "r"  it will raise an error if file not exist
file.close()

# WAP to add sth in file.


# w mode will erase the past all data nd write only new data.


file=open("student.txt","w")
file.write("This side harsh jaat")
file.close()
# if we want to add new data also nd old data should not be removed we will use a
file=open("student.txt","a")
file.write("\n ankit ch \n shubham sharma")
file.close()



# WAP to read data from the
file=open("student.txt",'r')
# data=file.read()  # read all data 
# data1=file.read(20)  # read 20 1st char
data2=file.read()
data3=file.readline()   # one line at a time 
# print(data)
print(data2)
print(data2)
file.close()


# Tell -> it will print the exact postion of the error

file=open('student.txt','r')
print(file.tell())
data=file.read()
print(data)
print(file.tell())
file.close()


"""
# Seek - it will skip the starting char




























