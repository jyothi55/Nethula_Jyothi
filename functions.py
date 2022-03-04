#function defination
def myname():
    print("hello")
myname();

#passing arguments
def myname1(a):
    print(a)
myname1(10);

#passing multiple arguments
def myname2(a,b,c):
     return a,b,c
myname2(20,30,40);

#orbitary arguments
def myname3(*a):
    print(a)
myname3(1,2,"cherry");

#keyword arguments:
def myname4(**a):
    return a
b=myname4(name="cherry",age=25,qual="btech");
print(b)
    