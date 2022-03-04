#tuple declaration and its functions
jyothi= (1,2,3.5,"sai",6+6j,True)
print(jyothi[2])

#repeatation
jyothi1= (1,2,3.5,"sai",6+6j,True)
print(jyothi1*3)

#concatination:
jyothi= (1,2,3.5,"sai",6+6j,True)
i=(1,2,3,4)
print(jyothi+i)

#membership
jyothi3= (1,2,3.5,"sai",6+6j,True)
print(2 in jyothi3)

#Methods
#Min:
cherry=(912,3,45,6,) 
print(min(cherry))
#max
print(max(cherry))
#sort
print(sum(cherry))

#list Comprehension::
t=(1,2,3,4,5,15,25,5,3)
t1=[x*2 for x in t if x==5]
t2=[x+3 for x in t if x!=2]
t3=[x-3 for x in range(1,20,2) if x>5]
print(t1)
print(t2)
print(t3)
