givList=[1,2,3,4,5,6,7,8,9,10,2,4,68,10,12,14,16,18,20,3,6,9,12,15,18,21,24,27,30,4,8,12,16,20,2428,32,36,40,5,10,15,20,25,30,35,40,45,50,6,12,18,24,30,36,42,48,54,60,7,14,21,28,35,42,49,56,63,70,8,16,24,32,40,48,56,64,72,80,9,18,27,36,4554,63,72,81,90,1020,30,40,0,70,80,90]
myList=[]
for value in givList:
    if value<50:
        myList.append(value)

print(myList)

print('removing duplicate')

unique=[];
for value in myList:
    if value not in unique:
        unique.append(value)

print(unique)
unique.sort()
print(unique)

print('let\'s try set')

mySet=set()
mySet=set(myList)
print(list(mySet))
