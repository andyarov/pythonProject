dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
for key, value in dict1.items():
    print(key,'->',value)
sum = sum(dict1.values())
print(sum)

dict1['f'] = None
print(dict1)
dict2 = [dict(dict1.items()) for value in dict1.values() if value != None]
print(dict2)