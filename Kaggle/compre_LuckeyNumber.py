
def luckeyChecker(mylist):
    return any([n%7==0 for n in mylist])

mylist=[10,12,4,73,8,31,35,4]
print("The list is luckey:",luckeyChecker(mylist))
