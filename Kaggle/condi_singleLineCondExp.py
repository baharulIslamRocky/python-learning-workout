
def result(mark):
    outcome='failed' if mark<50 else 'Passed'
    print('You',outcome,'the quize with a grade of',mark)



result(40)
result(54)
