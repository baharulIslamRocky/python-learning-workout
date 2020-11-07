
def multByfive(x):
    return 5*x

def singleCall(fn,arg):
    return fn(arg)

def dubleCall(fn,arg):
    return fn(fn(arg))

print(
    multByfive(2),#10
    singleCall(multByfive,2),#10
    dubleCall(multByfive,2),
    sep='\t'
    )#50
