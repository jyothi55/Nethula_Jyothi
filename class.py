"""class Jyothi:
    print("this is class")
    def display(self):
        a=10
        b=12
        print(a,b)
obj=Jyothi() # take one variable assign class name to it...called object
obj.display() """
#then call function with object.

"""class My_details:
    def __init__(self,id,designation,age) :
        self.jyothi_id=id
        self.jyothi_designation=designation
        self.jyothi_age=age
        def bio(self):
            print("id is",self.jyothi_id)
            print("designation is",self.jyothi_designation)
            print("age is",self.jyothi_age)
obj=My_details("101","software","25")
obj.bio()"""

class Mobile:
    def __init__(self,brand,battery):
       self.Brand=brand
       self.Battery=battery
    def display_2(self):
        print("brand",self.Brand)
        print("battery",self.Battery)
for i in range(5):
    obj=Mobile("apple",'4000mah')
    obj.display_2()
    print("...........")
    obj1=Mobile("ipn","300mah")
    obj1.display_2()


        

