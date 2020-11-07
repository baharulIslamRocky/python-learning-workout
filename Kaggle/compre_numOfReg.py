def count_negative(number):
    #count=[c for c in number if c < 0]
    ##return len(count)
    return len([c for c in number if c<0])

print(count_negative([5,-1,-2,0,3]))
