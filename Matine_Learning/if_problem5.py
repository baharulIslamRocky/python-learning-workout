latter=input('Enter an Character:')
if latter=='a' or latter=='A' or latter=='e' or latter=='E' or latter=='i' or latter=='I' or latter=='o' or latter=='O' or latter=='u' or latter == 'U' :
        print('%s is a vowel'%latter)
elif(latter>='a' and latter<='z') or (latter>='A' and latter<'z') :
        print("%s is a constant"%latter)
else:
    print('Nothing')
