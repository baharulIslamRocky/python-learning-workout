latter=input('Enter a Character: ')

if (latter>='a' and latter<='z') or (latter>='A' and latter<='Z'):
    if latter in 'AEIOUaeiou':
        print('%s is vowel'%latter)
    else:
        print('%s is constant'%latter)
else:
    print('Nothing')
