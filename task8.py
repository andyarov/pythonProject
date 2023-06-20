dgt = int(input())
def leap(dgt):
    if dgt % 400 == 0:
        return "leap year"
    elif dgt % 4 == 0 and dgt % 100 != 0:
        return "leap year"
    else:
        return "non-leap year"
print(leap(dgt))
