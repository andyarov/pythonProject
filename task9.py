# symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# strng = input()
# def remove_symbols(strng, symbols):
#     result = [i for i in strng if i not in symbols]
#     print(''.join(result))
#
# remove_symbols(strng, symbols)

def srt():
    words = [w.lower() for w in input().split(", ")]
    words.sort()
    return words
print(srt())