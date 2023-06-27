'''напишите программу викторину. функция принимает на вход ответ на вопрос
у пользователя есть право на три ошибки
за каждый ответ начисляется 1 балл
вывод: количество баллов'''

score = 0

'''def quiz(answer):
    global score
    tries = 2
    for i in range(3):
        inp_answer = input().lower()
        if inp_answer == answer:
            print('Your answer is correct')
            score += 1
            break
        elif tries != 0:
            print('Try again, you have {} tries'.format(tries))
            tries -= 1
            continue
        else:
            print('Your answers is not correct, you have {} tries'.format(tries))'''


def quiz(answer):
    global score
    tries = 3
    while tries != 0:
        inp_answer = input()
        if inp_answer.lower() == answer.lower():
            print('Your answer is correct')
            score += 1
            break
        else:
            tries -= 1
            if tries == 0:
                break
            print('Try again, you have {} tries'.format(tries))
            continue
    print('Your answers is not correct, you have {} tries'.format(tries))


quiz('2')
print('Your score =', score)
