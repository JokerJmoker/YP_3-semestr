# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer

def annoying_input_str(message=''):
    answer = None
    while answer is None:
        answer = input(message)
        if not isinstance(answer, str):
            print('Вы ввели недопустимые символы')
            answer = None
    return answer

def game_tournament(hero, enemy_list):
    for enemy in enemy_list:
        if isinstance(enemy, Dragon):
            print('Вышел', enemy._color, 'дракон!')
            while enemy.is_alive() and hero.is_alive():
                print('Вопрос:', enemy.question())
                answer = annoying_input_int('Ответ:')

                if enemy.check_answer(answer):
                    hero.attack(enemy)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    enemy.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if enemy.is_alive():
                break
            print('Дракон', enemy._color, 'повержен!\n')

        if isinstance(enemy, Trolle):
            print('Вышел', enemy._size, 'тролль!')
            while enemy.is_alive() and hero.is_alive():
                print('Вопрос:', enemy.question())
                answer = annoying_input_str('Ответ:')

                if enemy.check_answer(answer):
                    hero.attack(enemy)
                    print('Верно! \n** тролль проклинает вашу мудрость **')
                else:
                    enemy.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if enemy.is_alive():
                break
            print('Тролль', enemy._size, 'повержен!\n')

        else:
            print ("искусственный интеллект ")
        



    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        enemy_number = 1
        enemy_list = generate_enemy_list(enemy_number)
        assert(len(enemy_list) == 1)
        print('У Вас на пути', enemy_number, 'врагов!')
        game_tournament(hero, enemy_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
