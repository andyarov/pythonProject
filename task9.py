symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
strng = input()
def remove_symbols(string, symbols):
    result = [i for i in string if i not in symbols]
    return result

print(remove_symbols(strng, symbols))