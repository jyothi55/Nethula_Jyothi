#compiletime polymorphism
#a.method overloading
#same class
#same function or methods
#different parameters
"""class A:
    def myfunction(self,a,b):
        print(a*b)
    def myfunction(self,a,b,c=1):# overcome by giving default value
        print(a*b*c)
obj=A()
obj.myfunction(2,2)"""

#runtime polymorphism(dynamic)
#a. method overriding
# same function name
#different parameters
#different classes
class A:
    def hello(self,a,b,c,d):
        return a+b+c+d
class B(A):
     def hello(self,a,b):
         super().hello(3,4,5,6)
         print(a+b)  
obj=B()
obj.hello(1,3) 
