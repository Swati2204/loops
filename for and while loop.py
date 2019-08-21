'''syntax for for loop
for variable in sequence:  '''
# Program to print squares of all numbers present in a list
numbers = [1, 2, 3, 4, 15, 20]
for i in numbers:
    sq = i * i
    print(sq)

#program to print number from 1 to 20
i=1
for i in range(1,21):
    print(i)
    
''''syntax for while loop
while condition:
    #body_of_while'''
#program using while loop
i=1
s=0
while i<6:
    s=s+i
    i=i+1
    print(s)
