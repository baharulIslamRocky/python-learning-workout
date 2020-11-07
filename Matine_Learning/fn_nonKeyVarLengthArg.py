

def keyWord(**c):
    """
        it's dictionary
        create variable as we want    """
    total=count=0;
    for paise in c:
        count+=1
        total+=c[paise]
        print("c[%s]=%d"%(paise,c[paise]),end=', ')
    print()
    return total
print("sum=",keyWord(a=1))
print("sum=",keyWord(a=1,b=2))
print("sum=",keyWord(a=1,b=2,c=3,d=4))
print("sum=",keyWord(a=1,b=4,c=5))
