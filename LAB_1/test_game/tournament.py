# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message=''):
    answer = None
    while answer is None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы.')
    return answer

def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print(f'Вышел {dragon._color} дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ: ')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print(f'Дракон {dragon._color} повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили всех драконов!')
        print(f'Ваш накопленный опыт: {hero._experience}')
    else:
        print('К сожалению, Вы проиграли...')

def start_game():
    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        hero_name = input('Представьтесь, пожалуйста: ')
        hero = Hero(hero_name)

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        print(f'У Вас на пути {dragon_number} драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
