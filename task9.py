from itertools import chain
# symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# strng = input()
# def remove_symbols(strng, symbols):
#     result = [i for i in strng if i not in symbols]
#     print(''.join(result))
#
# remove_symbols(strng, symbols)

'''def srt():
    words = [w.lower() for w in input().split(",")]
    words.sort()
    return words
print(srt())'''


# result = []
# result = [i for lst in nested_list for i in lst]

'''for i in nested_list:
    for j in i:
        result.append(j)'''
nested_list = [['a', 'b', 'c', 'd', 'e', 'f']]
result = list(chain(*nested_list))
print(result)