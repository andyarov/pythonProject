# напишите функцию календарь, на вход год, месяц, и число, число(опциональный аргумент)

'''def calendar(yyyy, mm, dd=''):
    print('Today is {}/{}/{}'.format(dd, mm, yyyy))


calendar(1000, 12, 3)
'''

'''def insects(*args):
    print(args)
    
insects('жесткокрылые', 'двукрылые', 'чешуекрылые', 'перепончатокрылые')
'''

'''def print_hello():
    strng = "Привет питонист!"

    def print_str():
        print(strng)

    print_str()


print_hello()'''

'''strng = input()

def letters_counter(st):
    vowels = 'AaEeIiOoUuYy'
    vowels_letters = [letters for letters in st if letters in vowels]
    consonants_letters = [letters for letters in st if letters not in vowels]
    print('vowels: ', len(vowels_letters))
    print('consonants: ', len(consonants_letters))


letters_counter(strng)'''
'''Нужно вывести первые n строк треугольника Паскаля.
В этом треугольнике на вершине и по бокам стоят единицы, 
а каждое число внутри равно сумме двух расположенных над ним чисел.'''


def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


pascal_triangle(6)