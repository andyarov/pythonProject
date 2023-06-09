n = int(input("введите число: "))
if n > 0:
    lst = range(n+1)
elif n < 0:
    lst = range(n,n*-1+1)
for i in lst:
    if i == 0:
        continue
    elif n % i == 0:
        print(i)
    else:
        continue