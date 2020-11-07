
def mulBy2(x):
    return 2*x

def square(fn,x):
    return fn(fn(x))

def qube(fn,x):
    return fn(fn(fn(x)))

def quad(fn,x):
    return fn(fn(fn(fn(x))))



print(mulBy2(2),square(mulBy2,2),qube(mulBy2,2),
      quad(mulBy2,2),
      square(mulBy2,2)*square(mulBy2,2),sep='\n')
