list1 = []
for i in range(1,1001):
    square = i ** 2
    list1.append(square)
print(list1)
qt = 0
list2 = []
for item in list1:
    item = str(item)
    list2.append(item)
print(list2)
for b in list2:
    if '20' in b:
        digit = (list2[b])
        list2.remove(digit)
        qt += 1
print(list1)
print("Количество удаленных чисел: ", qt)