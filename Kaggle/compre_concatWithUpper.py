planet=['Marcury','Venus','Earth','Mars','Jupitar','Saturn','Uranus','Neptune']

upperConcat=[name.upper()+'R'for name in planet if len(name)<6]
print(upperConcat)
