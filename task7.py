dgt, keyw = input().split()
dgt = int(dgt)
def conv(dgt, keyw):
    if keyw == 'F':
        deg = (dgt - 32) / 1.8
    elif keyw == 'C':
        deg = dgt * 1.8 + 32
    return deg
print(conv(dgt, keyw))