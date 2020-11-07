
def defaultArgument(a,b,c=3):
    """
    if third argument value not given from
    caller function ,then c is automatically 3.
    """
    print("a=",a,"b=",b,"c=",c)
    return a+b+c


print(defaultArgument(10,20))
print(defaultArgument(10,20,40))
