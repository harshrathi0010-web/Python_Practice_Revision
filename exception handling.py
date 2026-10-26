"""

Exception Handling--> try,except,finally

Try:
    your doubtful code here

except:
        Alternate code

# Try cannot work alone we have to use also except,finally

try:
    a=int(input("enter the num1:"))
    b=int(input("enter the num2:"))
    
    print("Divison",a/b)
except ZeroDivisionError as e:
    print("Error",e)

except ValueError as e:
    print("Error:",e  )

print("Program Ended!")



try:
    a=int(input("enter the num1:"))
    b=int(input("enter the num2:"))
    
    print("Divison",a/b)


except Exception as e:         # Exception is the master of all error
    print("Error:",e  )

finally:
    print("ye to hmesa chlega")
    
print("Program Ended!")



# give error name according to situation

class AgeError(Exception):
    pass

age=int(input("enter your age:"))
if age>17:
    print("welcome")
else:
    raise AgeError("age should be 17+")

    
"""




    
    


