
string=input('enter a string: ')

lString=string.casefold()
revString=lString[::-1]

if revString==lString:
    print("it's palinedrome")
else:
    print("Not palinedrome!")
