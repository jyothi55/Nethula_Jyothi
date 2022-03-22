from datetime import datetime
name=input("Enter your name:")
# list of items::
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
salt    Rs 40/kg
oil     Rs 80/ltr
paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 85/each
'''
#declaration::
price=0
pricelist=[]
totalprice=0
finalamount=0
ilist=[]
qlist=[]
plist=[]

#rates for items::
items={'Rice':20,'Sugar':30,'salt':20,
'oil':80,'paneer':110,'Maggi':50,
'Boost':90,'Colgate':85}
option=int(input("For list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items")
        quantity=int(input("Enter your quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("Can i bill the items??::yes or no     ")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Cherry's supermarket",25*'=')
            print(28*" ","siricilla")
            print("Name:",name,30*" ",'Date:',datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',15*" ",'price')
            for i in range(len(plist)):
                print(i,6*' ',3*' ',ilist[i],10*' ',qlist[i],19*" ",plist[i])
                print(75*"-")
                print(50*" ",'TotalAmount:','RS',totalprice)
                print("gst amount",50*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'finalAmount:','Rs',finalamount)
                print(75*"-")
        print(25*" ","Thanks for visiting",25*" ")
        print(75*"-")



