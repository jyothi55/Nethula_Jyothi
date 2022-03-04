#List defination and its methods
#append
jyothi=[1,2,3.5,"jyothi",[34,56,89],8+4j,True]
jyothi.append(30)
print(jyothi[4][2])
print(type(jyothi))

#extend
jyothi_1=[1,2,3.5,"jyothi",8+4j,True]
jyothi_1.extend([50,30,"cherry"])
print(jyothi_1)

#remove
jyothi_2=[1,2,3.5,"jyothi",8+4j,True]
jyothi_2.remove("jyothi")
print((jyothi_2))

#insert
jyothi_3=[1,2,3.5,"jyothi",8+4j,True]
jyothi_3.insert(4,'choty')
print((jyothi_3))

#count::
jyothi_4=[1,1,2,2,3.5,"jyothi",8+4j,True]
print((jyothi_4.count("jyothi")))

#len::
print(len(jyothi_4))

#pop:
jyothi_5=[1,1,2,2,3.5,"jyothi",8+4j,True]
jyothi_5.pop(4)
print(jyothi_5)

#reverse
jyothi_6=[1,1,2,2,3.5,"jyothi",8+4j,True]
jyothi_6.reverse()
print(jyothi_6)

#sort:
jyothi_7=[1,20,4,7,9,89]
jyothi_7.sort()
print(jyothi_7)



