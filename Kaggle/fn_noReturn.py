
def leastDifference(a,b,c):
    """ return the smallest difference among
        a,b,c.
        >>>> 1,5,7   ## comment doc string
                    ##and execute help(leastDifference) and see
        >>>>2
    """
    dif1=abs(a-b)
    dif2=abs(b-c)
    dif3=abs(c-a)
    min(dif1,dif2,dif3)

##print(leastDifference(1,5,11))

print(leastDifference(1, 10, 100), leastDifference(1, 10, 10),leastDifference(5, 6, 7))
