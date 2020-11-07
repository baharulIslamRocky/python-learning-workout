
def countEven(kaggleList):
     return len([count for count in kaggleList if count%2==0])
    

kaggleList=[1,2,3,4,5,6,7,8,9]
print(countEven(kaggleList))
#co=len([count for count in kaggleList if count%2==0])
#print(co,type(co),sep='---')
