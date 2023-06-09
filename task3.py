list1 = []
qt = 0
for i in range(1,1001):
    square = i ** 2
    if '20'  not in str(square):
        list1.append(square)
    else:
        print(square)
print(1000 - len(list1))

