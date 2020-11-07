
def inspect(num):
    if num == 0 :
        print(num,'is Zero')
    elif num>0 :
        print(num,'is Positive')
    elif num <0 :
        print(num,'is Negative')
    else:
        print(num,'is unlike anythinng i have ever seen')

num=int(input("Enter a number:"))

inspect(num)
