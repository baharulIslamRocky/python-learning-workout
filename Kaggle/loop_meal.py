
def menuIsBoring(l):
    print(l)
    for n in range(len(l)):
        print(n)
        if n>0 and l[n]==l[n-1]:
            print('!')
            return True
    return False
       



print(menuIsBoring(['rice','egg','chiken','rice','rice']))
