
def seriesAdd():
    a=int(input("Enter starting of series: "))
    b=int(input("Enter end  of series: "))
    res=0
    for value in range(a,b+1):
        res+=value
    else:
        print('the summation from {} to {} is {}'.format(a,b,res))
    again=int(input("wanna play again press 1:"))
    if again==1:
        print('\n')
        seriesAdd()
    menu()
    print('\n')

def namta():
    a=int(input("Enter starting of namta: "))
    b=int(input("Enter end  of namta: "))
    res=0
    for i  in range(a,b+1):
        for j in range(1,11):
            res=(i*j)
            print('{} x {} = {}'.format(i,j,res))
        else:
            print('----------------------')
    again=int(input("wanna play again press 1:"))
    if again==1:
        print('\n')
        namta()
    menu()
    print('\n')

def evenOdd():
    a=int(input("Enter starting of series: "))
    b=int(input("Enter end  of series: "))
    li=list(range(a,b+1))
    print("Print all ODD between %d to %d"%(a,b))
    for i in li :
        if i%2==0:
            continue
        print(i)
    print("Print all even between %d to %d"%(a,b))
    for i in li :
        if i%2==1:
            continue
        print(i)
    again=int(input("wanna play again press 1:"))
    if again==1:
        print('\n')
        evenOdd()
    menu()
    print('\n')

def divided():
    a=int(input("Enter starting of series: "))
    b=int(input("Enter end  of series: "))
    li=list(range(a,b+1))
    res=list()
    for i in li:
        if i%5==0 and i%10!=0 :
            res.append(i)
    else: print(res)
    again=int(input("wanna play again press 1:"))
    if again==1:
        print('\n')
        divided()
    menu()
    print('\n')
def palinedrome():
    char=(input('Enter a word: '))
    ch=char.casefold()
    rev=ch[::-1]
    if ch == rev :
        print("{} is a palinedrome word".format(char))
    else: print("{} is NOT  a palinedrome word".format(char))

    again=int(input("wanna play again press 1:"))
    if again==1:
        print('\n')
        palinedrome()
        
    menu()

def binarySearch():
    print('make the list: ')
    start=int(input('Enter starting: '))
    end=int(input('Enter ending: '))
    increment=int(input('enter increment step of series: '))
    search=int(input('Enter the number that position you wanna search in series: '))
    series=list(range(start,end+1,increment))
    print(series)
    size=list(range(len(series)//2))
    mid=len(series)//2
    for i in size:
        if search<series[mid]:
            end=mid
        elif search>series[mid]:
            start=mid
        else :
            print ("the position of {} is at {} ".format(search,mid+1))
            print('Validation check {}'.format(series.index(search)+1))
            break;
        mid=(start+end)//2
    print(start,mid,end)
    again=int(input("wanna play again press 1:"))
    if again==1:
        print('\n')
        binarySearch()
        
    menu()
    
def menu():
    print("enter your choise:")
    print('Press 1 for add a series number','Press 2 for check Namta to 10 times','Press 3 for even odd from a series:','Press 4 show the number of a series that divided by 3 but not 5','Press 5 for Palinedrome ','Press 6 for Binary search',sep='\n')
    choice=int(input('\nyour choice:'))
    if choice==1:
        seriesAdd()
    elif choice==2:
        namta()
    elif choice==3:
        evenOdd()
    elif choice==4:
        divided()
    elif choice==5:
        palinedrome()
    elif choice==6:
        binarySearch()
    else:print("\nWrong choice!")
    '''elif choice==5:
        leapYear()'''
    
menu()
