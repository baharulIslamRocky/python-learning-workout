
def eligiblePresident(age,bornInHomeland):
    """
    bornInHomeland is bool is do 'and' operation with
    age and return true ,false
    """
    return (age>=35) and bornInHomeland


print("Stutus:",
      eligiblePresident(19,True),
      eligiblePresident(45,False),
      eligiblePresident(40,True),
      eligiblePresident(19,False),
      sep='\n\t')
