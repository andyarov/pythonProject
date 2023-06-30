# напишите функцию календарь, на вход год, месяц, и число, число(опциональный аргумент)

def calendar(yyyy, mm, dd=''):
    print('Today is {} {} {}'.format(dd, mm, yyyy))


calendar(1000, 12, 3)
