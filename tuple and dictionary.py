tuple = ("apple", "banana", "cherry")
print(tuple[1])

numbertuple = ("45", "66", "58")
if "58" in numbertuple:
print("Yes,'58' is in the number tuple")

tuplea=(523,'Rahul','riya')
print(type(tuplea))  
print(len(tuplea))   
tuple1=(109,'prakas','janak')
tuple2=(19,5,6,1)
tuple3=[4,5,6,7]
print(type(tuple3))

#indexing and slicing of tuples.

print(tuple1[:]) 
print(tuple2[0:])
print(tuple3[0:2])
print(tuple1[-1])
print(tuple3[:-1])

del(tuple3) 

print(tuple2*2) 

print(tuple2+tuple1) 

thisdict =	{
  "name": "swati",
  "course": "b.tech",
  "year": 2018-19
}
print(thisdict)
for x, y in thisdict.items():
  print(x, y)
thisdict =	{
  "name": "swati",
  "course": "b.tech",
  "year": 2018-19
}
print(thisdict)
thisdict.popitem()
print(thisdict)
