listt=[];
for value in range(1,101):
    if(value%3==0 and (not value%5==0)):
        listt.append(value);

print (listt)
