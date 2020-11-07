

num=int(input('enter a number:'))



def checkNumber(num):
    if num>0:
        print(num,'is Positive')
    elif num<0:
        print(num,'is negative')
    elif num==0 :
        print(num, 'is zero')
    else:
        print('it\' not number')
        
checkNumber(num)        
