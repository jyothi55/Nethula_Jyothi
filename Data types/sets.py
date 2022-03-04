s={1,1,2,3,4,5.9,"cherry",True}
s.add("cherry")
print(s)
s.update(["python"])
print(s)
s.remove("python")
print(s)

#set operations
s1={1,2,3,45,6}
s2={5,6,7,8,9}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))