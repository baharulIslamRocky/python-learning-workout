
def greaterThan(L,thresh):
    return [n>thresh for n in L]


#print(greaterThan([1, 2, 3, 4], 2))


def gt(L,thresh):
    num=[n for n in L if n>2]
    return num

print(gt([1, 2, 3, 4], 2))
