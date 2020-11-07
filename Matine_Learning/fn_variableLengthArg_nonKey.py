

def nonKey(*a):
    """
    create as need of argument
    create a tuple
    so it's non key
    
    """
    total=count=0

    for item in a:
        print(item,end="-")
        total+=item
        count+=1
    print()
    print('count=',count)
    return total


print('sum= ',nonKey(1))
print('sum= ',nonKey(1,2))
print('sum= ',nonKey(1,2,3,4,5))
print('sum= ',nonKey(1,2,3))
