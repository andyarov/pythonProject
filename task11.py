# напишите функцию календарь, на вход год, месяц, и число, число(опциональный аргумент)

'''def calendar(yyyy, mm, dd=''):
    print('Today is {}/{}/{}'.format(dd, mm, yyyy))


calendar(1000, 12, 3)
'''

'''def insects(*args):
    print(args)
    
insects('жесткокрылые', 'двукрылые', 'чешуекрылые', 'перепончатокрылые')
'''


def print_hello():
    strng = "Привет питонист!"

    def print_str(st):
        print(st)

    print_str(strng)


print_hello()
