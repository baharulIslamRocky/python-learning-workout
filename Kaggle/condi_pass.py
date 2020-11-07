
def result(mark):
    if mark<50:
        outcome='failed'
    else:
        outcome='Passed'
    print("you",outcome,'the quize with  a grade of ',mark)

result(45)
result(90)
