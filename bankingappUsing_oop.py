#Parent class :User
# 1.Holds details about a user
# 2.Has a function to show user details

#Child class:Bank
# 1.stores details about accont balance
# 2.Stores details about the amount
# 3.Allows for deposits,withdrawls,view_banlace functions

#Parent Class
class User():
  def __init__(self,name,age,gender):
      self.name=name
      self.age=age 
      self.gender=gender
  def show_user_details(self):
    print("Personal Details::")
    print("")
    print("Name",self.name)
    print("age",self.age)
    print("gender",self.gender)
#Child class::
class Bank(User):
  def __init__(self,name,age,gender):
    super().__init__(name,age,gender)
    self.balance=0
  def deposit(self,amount):
    self.amount=amount
    self.balance=self.balance+self.amount
    print("Account balance has been updated RS/-" ,self.balance)
  def withdraw(self,amount):
    self.amount=amount
    if self.amount>self.balance:
      print("Insufficient Funds  | Balance availabe : RS/-",self.balance)
    else:
      self.balance=self.balance-self.amount
      print("Account balance has been updated:RS/-",self.balance)
  def view_balance(self):
    self.show_user_details()
    print("Account balance :RS/-",self.balance)
    





