"""
Binary file handling--> It stores that data object by object......
format--> .dat,.bin etc.

file_handler=open("file_name",'mode')
mode--> r,a,w,r+,w+,a+

example-->

file=open('employee.bin','wb')
file.close()


# we need a library JOBLIB/PICKLE

    # dump- It is used to write data into binary file
    #   load- It is use to read data from a binary file.

import pickle
file=open('employee.bin','rb')
pickle.dump("this side harsh rathi for the interview",file)
data=pickle.load(file)
print(data)
file.close()

import pickle
file=open('employee.bin','rb')
try:
    while True:
        data=pickle.load(file)
        print(data)
except:
    print("\n Data Read Successfully!")
file.close()

"""








