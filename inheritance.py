#single inheritance::
"""class Parent:
    a=10
    print(a)
class Child(Parent):
    def fun1(self):
        print("hello i am child")
obj=Child()
obj.fun1()"""

# Multi -Level Inheritance::
"""class Parent_1:
    def mychilds(self):
        print("  i am parent for my childs")
class Child_1(Parent_1):
    def function(self):
        print("hello i am child")
class Grand_Child_1(Child_1):
    def function1(self):
        print("hello i am grandchild")
obj=Grand_Child_1()
obj.mychilds()
obj.function()
obj.function1()"""

#heiraricle inheritance::

"""class Parent_2:
    def mychilds__(self):
        print("  i am parent for my childs b and c")
class Child_B(Parent_2):
    def function__(self):
        print("hello i am child b")
class Child_C(Parent_2):
    def function1___(self):
        print("hello i am child c")
obj1=Child_C()
obj2=Child_B()
obj1.function1___()
obj1.mychilds__()
obj2.function__()
obj2.mychilds__()"""


#MULTIPLE inheritance:::
"""class Parent_1:
    def mychilds(self):
        print("  i am parent for my childs")
class Child_1(Parent_1):
    def function(self):
        print("hello i am child")
class Grand_Child_1(Child_1):
    def function1(self):
        print("hello i am grandchild")
obj=Grand_Child_1()
obj.mychilds()
obj.function()
obj.function1()"""

#heiraricle inheritance::

"""class Mom:
    def mom_prop(self):
        print("  i am parent of jyothi**")
class Dad:
    def  dad_prop(self):
        print("i am father of jyothi@@@")
class Me(Mom,Dad):
    def my_function(self):
        print("i am child of Mom and dad")
my_obj=Me()
my_obj.my_function()
my_obj.dad_prop()
my_obj.mom_prop()"""

#super keyword
class A:
    def __init__(self):
        print("hello___1")
    def fun1(self):
        print("fuction1")

class B(A):
    def __init__(self):
        print(" hello___2")
        super().__init__()
    def fun2(self):
        print("function2")
        super().__init__()
obje=B()


        








