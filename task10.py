'''напишите программу викторину. функция принимает на вход ответ на вопрос
у пользователя есть право на три ошибки
за каждый ответ начисляется 1 балл
вывод: количество баллов'''

score = 0


def quiz(answer):
    global score
    for i in range(3):
        inp_answer = int(input())
        if inp_answer == answer:
            print('Your answer is correct')
            score += 1
            break
        else:
            print('Your answer is not correct, try again')
            continue


quiz(2)
print(score)
