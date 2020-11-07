
def seriesAdd():
    a=int(input("Enter starting of series: "))
    b=int(input("Enter end  of series: "))
    res=0
    for value in range(a,b+1):
        res+=value
    else:
        print('the summation from {} to {} is {}'.formate(a,b,res))

def menu():
    print("enter your choise:")
    print('Press 1 for add a series number','Press 2 for check upper case/ lower case','Press 3 for check constant/vowel','Press 4 for school grade','Press 5 for leap year',sep='\n')
    choice=int(input('\nyour choice:'))
    if choice==1:
        seriesAdd()
    elif choice==2:
        upperLower()
    elif choice==3:
        constantVowel()
    elif choice==4:
        grade()
    else:print("\nWrong choice!")
    '''elif choice==5:
        leapYear()'''
    
menu()
