

'''def name(nam='shila'):
    print('my name is',nam);
    return


name('rockey')
name()'''

"""
def multiple(n):
    return n*5

def square(fn,n):
    return fn(n)

def qube(fn,n):
    return fn(fn(n))

print(square(multiple,1))
print(qube(multiple,1))
"""
'''
def modBy5(n):
    return n%5

print(max(12,13,14))
print(max(12,13,42,key=modBy5))
'''
"""
def smash_candies(total,friends=3):
    return total%friends

print('need to smash:',smash_candies(80,4))
print('need to smash:',smash_candies(82))

"""

"""

def runForPresident(age):
    return age>=35

print( runForPresident(35))
print(runForPresident(34))
print(runForPresident(10))
print(runForPresident(88))

"""
"""
def oddcheck(num):
    return num%2==1
print(oddcheck(22))
print(oddcheck(21))
"""
'''
def runForPresedent(age,citizen):
    return age>=35 and citizen

print(runForPresedent(35,False))
print(runForPresedent(35,True))
print(runForPresedent(24,True))
print(runForPresedent(89,True))
'''
'''
def result(num):
    res='passed' if num>=40 else 'Failed'
    return res
num=34
print('you Result status:',result(num),'With a grade:',num)
num=44
print('you Result status:',result(num),'With a grade:',num)
'''
'''
def smash(num):
    return num%3
num=10
print('Spliting', 'candie' if smash(num)<2 else 'Candies')

num=14
print('Spliting', 'candie' if smash(num)<2 else 'Candies')
'''

#list
"""

x=.25
numeretor,demirator=x.as_integer_ratio()
print(numeretor,'/',demirator)
"""
#loop
'''
planet=['Marcury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
for name in planet:
    print(name,end='--')
'''
'''
string='steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
for char in string:
    if char.isupper():
        print(char,end='')
'''
'''
def n_negative(nums):
    return [number for number in nums if number <0]
def negative(nums):
    return len([numbers for numbers in nums if numbers<0])
nums=[10,20,-2,-5,4,-8,10,-5,78]
print(n_negative(nums))

print('number of negative:',negative(nums))
'''
'''
sen='hello \n rockey'
print(sen)
'''
'''
name=input('Enter your name: ')
greeting='Hello'
cgpa=13.06585454
money=4425541245421
print("{}Mr.{} good morning,\n you have CGPA of {:.3}and taka of {:,} \nGood bye {}".format(
greeting,name,cgpa,money,name))
'''

'''
planet='pluto'
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3}  {:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass,pluto_mass / earth_mass, population,
))
'''


'''
string='she is crazy but she is mine'
str=string.split()
print(str)
'''

document=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
keyword='casino'
indices=[]
for i,doc in enumerate(document):
    #print(doc,i,sep='--')
    tokens=doc.split()
    print(tokens)
    normalized=[token.lower()for token in tokens]
    print(normalized)
    
