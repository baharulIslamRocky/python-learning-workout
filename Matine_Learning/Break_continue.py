print(list(range(1,22)))
for item in range(1,22):
    if(item==21):
        print("it's 21")
        break
    elif(item %2==0):
        continue
    print(item)
