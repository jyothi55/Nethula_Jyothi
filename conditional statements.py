    #a==b
    #a!=b
    #a<=b
    #a>=b
from ast import And


a=1
b=3
if a<b:
 print("a is smaller than b")
elif a<b:
     print("a is smaller than b:::")
     
else:
    print("b is smaller than a")


#short hand if::
a=90
b=70
if a>b: print("this is short hand if")
#short hand if else:
print("this is short hand if staement") if a<b else print("this is short hand if else")

#logical operators::
num1=20
num2=40
num3=60
if num1>=num2 or num1>=num3:
    pass
    #print("the number is",num1)
elif num2!=num1 and num3>num2:
    print("the number is :",num2)
else:
    print("the number is",num3)

