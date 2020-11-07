
listOne=[i for i in range(11)]
print(listOne)
listTwo=[i for i in range(11,21)]
print(listTwo)
listFour=[i for i in range(21,31)]
listThree=zip(listOne,listTwo,listFour)

print(type(listThree))

print(list(listThree))

