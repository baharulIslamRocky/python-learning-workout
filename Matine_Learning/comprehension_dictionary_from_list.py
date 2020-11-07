critiria=['name','city','profession','mobile','country']
data=['ghurii','Bagerhat','student',443344,'Bangladesh']

buildDic={j:i for i,j in zip(critiria,data)}
print(type(buildDic))
print(buildDic)
