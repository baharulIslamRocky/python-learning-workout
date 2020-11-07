
print('Enter total number of candies:')
total=int(input())

def smashNumber(num,friends=3):
    return num%friends

print("need to smash:",smashNumber(total,4))
