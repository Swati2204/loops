#ways to create strings in Python
str = 'hello'
print(str)

str2 = "friends"
print(str2)

# multi-line string
str3 = """Welcome to 
   the world of python"""
print(str3)

print(type(str))    
print(len(str2))

# Indexing and slicing in strings.

print(str3[:])       
print(str3[0:])
print(str2[:6])
print(str3[0])
print(str[1])
print(str[2])
print(str1[3])
print(str3[0:5])
print(str[1:3])
print(str3[-5])  
print(str3[:-1])

# concatenation of string
a="python"
b="learning"
print(a+b)

#Repetition of string 
a="python"*3
print(a)

a="student"
b="swati shrivastav"
c="btech"
print(a.lower())  

print(b.upper()) 

print(b.title()) 

print(c.capitalize()) 

print(b.count('a'))  

print(a.isupper())

print(c.islower())  

print(c.istitle())  

print(a.index('a'))

#list in python

lista=[71,52,93,46,58,93]
listb=['swati','shreya','priya']
str='python world'

print(max(lista))  

print(min(lista)) 

print(list(str)) 

listb.append('supriya')  
print(listb)

lista.insert(2,'88') 
print(lista)

listb.reverse() 
print(listb)

listb.copy()  
print(listb)

lista.remove(52) 
print(lista)

listb.pop()  
print(lista)

listb.clear() 
print(listb)


# indexing and slicing in list
list1=['priya','swati','pari','ruby']
list2=[44,90,99,80,67,45,89]
list3=['abc','bbc','name','rollno','ddr']
print(list1[:])       
print(list3[0:])
print(list1[:3])
print(list2[0])
print(list2[1])
print(list1[0:1])
print(list3[2:3])
print(list2[-1])  
print(list1[:-1])


