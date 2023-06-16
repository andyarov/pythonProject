dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
sum = 0
for key, value in dict1.items():
    print(key,'->',value)
    sum += value
print(sum)