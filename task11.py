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

'''tallies = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_decimal(roman_number):
    sum = 0
    for i in range(len(roman_number) - 1):
        left = roman_number[i]
        right = roman_number[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[right]
    sum += tallies[roman_number[-1]]
    return sum


print(roman_to_decimal("III"))'''
