symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
strng = input()
def remove_symbols(strng, symbols):
    result = [i for i in strng if i not in symbols]
    return print(''.join(map(str, result)))

remove_symbols(strng, symbols)