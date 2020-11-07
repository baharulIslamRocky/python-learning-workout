
def eligible(age,born):
    return (age>=35 and born)

age=int(input("enter your age:"))
born=bool(int(input("if you born in this country then press 1,otherwise press 0: ")))
print(born)
print("you're eligible for President:",eligible(age,born))

