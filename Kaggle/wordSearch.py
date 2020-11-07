
def wordCheck(document,keyword):

    index=[]

    for i,doc in enumerate(document):

        tokens=doc.split()
        single=[item.rsplit(',.').lower() for item in tokens]
        if keyword.lower() in single:
            index.append(i)
    return index
