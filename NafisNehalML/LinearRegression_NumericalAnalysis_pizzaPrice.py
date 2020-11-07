
pizzaSize=[6,8,12,14,18]#x indipendent
pizzaPrice=[350,775,1150,1395,1675]#y dependent
xSqrSum=xSum=ySum=xySum=0
#print(xSqrSum,xSum,ySum,xySum)
for x in pizzaSize:
    xSqrSum+=x**2#x2bar
    
    xSum+=x#xbar
for y in pizzaPrice:
    ySum+=y#ybar
for i in range(len(pizzaSize)):
    #print (i)
    xySum=xySum+(pizzaSize[i]*pizzaPrice[i])#(xy)bar
    #print(x**2)

#print(len(pizzaPrice),'----',len(pizzaSize))    
xbar=float(xSum)/float(len(pizzaSize))
#print(xSum,'xbar',xbar)

ybar=float(ySum)/float(len(pizzaPrice))
#print(ySum,'ybar',ybar)

xybar=float(xySum)/float(len(pizzaSize))
#print(xySum,"xybar",xybar)

xSqrBar=float(xSqrSum)/float(len(pizzaSize))
#print(xSqrSum,'xSqrbar',xSqrBar)
m=float((xbar*ybar)-xybar)/((xbar**2)-xSqrBar)
c=ybar-(m*xbar)
print("The Regression /Best_fit  Line:y={:.5}x + ({:.5})".format(m,c))

new=int(input('Enter new Size and get that the price: '))
print("The {}inch pizza price is ={:.7}".format(new,(m*new)+c))

print("calculating the regression Line R-Square value,,, ,, ,")
rSqr=upper=lower=0
for i in range(len(pizzaSize)):
    #print('y= ',((m*pizzaSize[i])+c),'!sqr= ',(((m*pizzaSize[i])+c)-ybar),'upper= ',(((m*pizzaSize[i])+c)-ybar)**2, 'LOwer= ',(pizzaPrice[i]-ybar)**2)
    upper+=float((((m*pizzaSize[i])+c)-ybar)**2)
    lower+=float((pizzaPrice[i]-ybar)**2)
    #print(rSqr)

print("your Regression line have {:.1%}accuracy".format(upper/lower))
