
def dif(a,b,c):
    """
    THIS  is an exaple
    it's return min distance.
    
    
    """
    a=abs(a-b)
    b=abs(b-c)
    c=abs(c-a)
    min(a,b,c)


n1=int(input())
n2=int(input())
n3=int(input())
print(dif(n1,n2,n3),
      dif(1,10,10),dif(5,6,7))
