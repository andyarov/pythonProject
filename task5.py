dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
for key, value in dict1.items():
    print(key,'->',value)
sum = sum(dict1.values())
print(sum)

dict1['f'] = None
print(dict1)
dict1 = {key:value for key, value in dict1.items() if value != None}
print(dict1)