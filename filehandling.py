f=open('g:/Jyothi/Python_Jyo/Data types/jyothi.txt','w')
content=f.write( "hello world")
print(content)
f.close()

f=open('g:/Jyothi/Python_Jyo/Data types/jyothi.txt','a')
content=f.write("i am cherry")
print(content)
f.close()

f=open('g:/Jyothi/Python_Jyo/Data types/jyothi1.txt','x')
content=f.write("i am cherry from hyd")
print(content)
f.close()

f=open('g:/Jyothi/Python_Jyo/Data types/jyothi.txt','r')
content=f.read()
print(content)
f.close()
