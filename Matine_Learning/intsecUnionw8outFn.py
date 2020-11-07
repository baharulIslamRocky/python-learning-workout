
a={1,2,3,5,4}
b={5,6,7,8}
print('Intersection:')
c=set()
for value in a:
    if value in b:
        c.add(value)
print(c)

print('Union')

c=set()
c.update(a)
c.update(b)
print(c)
