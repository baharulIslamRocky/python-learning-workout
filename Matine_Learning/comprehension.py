
roc_list=['rohim','jobbar','mamun','miraj','endat','a','bb','ccc','dd']
print(roc_list)
roc_set={name for name in roc_list if len(name)>2}
print(roc_set)
print('------------------------------------')
roc_tuple=(name for name in roc_list if len(name)>2)
print(tuple(roc_set))
