def mudolo_by5(x):
    return x%5
print(
    max(100,53,13),#100
    max(105,53,14,key=mudolo_by5),#54
    sep='~'
)
