

def keyWordArgument(a,b,c):
    """#based this argument name
    #value pass by on the name of variable
    #don't need any serial maintain from caller fn"""
    print("a=",a,"b=",b,"c=",c)
    return a+b+c

sum=keyWordArgument(b=1,c=3,a=2)
print(sum)
