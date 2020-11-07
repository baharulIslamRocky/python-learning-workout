def getNumber():
    number=int(input('Enter Number:'))
    return number

def getCharecter():
    char=input("Enter a charecter:")
    return char
    
def evenOdd():
    number=getNumber()
    if number%2==0:
        print(number,'is an even Number')
    elif number%2==1:
        print(number,'is an odd Number')
    else:
        print('This is not number')
    print('\n')
    again=int(input("wanna play again press 1:"))
    if again==1:
        evenOdd()
    menu()
    print('\n')

def constantVowel():
    char=getCharecter()
    lis=['a','e','i','o','u','A','E','I','O','U']
    if char in lis:
        print(char ,'is an vowel')
    elif (char>='a' and char<='z') or (char>='A' and char <='Z'):
        print(char,'is a Constant')
    else:
        print('Wrong input')
    print('\n')
    again=int(input("wanna play again press 1:"))
    if again==1:
        constantVowel()
    print('\n')
    menu()
    
    
def upperLower():
    char=getCharecter()
    if char>='a' and char<='z':
        print(char ,'is a lower case charecter')
    elif char>='A' and char <='Z':
        print(char ,'is a upper case charecter')
    else:
        print('Wrong input')
    print('\n')
    again=int(input("wanna play again press 1:"))
    if again==1:
        upperLower()
    print('\n')
    menu()

def grade():
    number=getNumber()
    if number>=80: print('A+')
    elif number>=75: print('A')
    elif number>=70: print('A-')
    elif number>=65: print('B+')
    elif number>=60: print('B')
    elif number>=55: print('B-')
    elif number>=50: print('C+')
    elif number>=45: print('C')
    elif number>=40: print('C-')
    elif number<=39 and number >=0: print('Failed')
    else: print('Wrong input')
    print('\n')
    again=int(input("wanna play again press 1:"))
    if again==1:grade()
    print('\n')
    menu()
    
def menu():
    print("enter your choise:")
    print('Press 1 for even/odd','Press 2 for check upper case/ lower case','Press 3 for check constant/vowel','Press 4 for school grade','Press 5 for leap year',sep='\n')
    choice=int(input('\nyour choice:'))
    if choice==1:
        evenOdd()
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
