
start=int(input("Enter an start value:"))
end=int(input("Enter an end value:"))
increment=int(input("Enter increment value:"))
summation=0
for value in range(start,end,increment):
    # print(value)
    summation+=value
print(summation)
