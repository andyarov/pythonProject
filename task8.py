'''dgt = int(input())
def leap(dgt):
    if dgt % 400 == 0:
        return "leap year"
    elif dgt % 4 == 0 and dgt % 100 != 0:
        return "leap year"
    else:
        return "non-leap year"
print(leap(dgt))'''

n = int(input())
m = int(input())
k = int(input())

def choco(n,m,k):
    if n*m < k:
        return 'size error'
    elif k % n == 0 or k % m ==0:
        return 'Yes'
    else:
        return 'No'
print(choco(n,m,k))