# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass

def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy

def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for _ in range(enemy_number)]
    return enemy_list

class Dragon(Enemy):
    def __init__(self, color):
        super().__init__(health=100, attack=30)  # Задаем здоровье и атаку дракона
        self._color = color
        self.__answer = None
        self.__quest = None
        
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
    
    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        return x, y 

class GreenDragon(Dragon):
    def __init__(self):
        super().__init__('зелёный')

    def question(self):
        x, y = super().question()
        self.__quest = f'{x} + {y}'
        self.set_answer(x + y)
        return self.__quest
    
class RedDragon(Dragon):
    def __init__(self):
        super().__init__('красный')

    def question(self):
        x, y = super().question()
        self.__quest = f'{x} - {y}'
        self.set_answer(x - y)
        return self.__quest
    
class BlackDragon(Dragon):
    def __init__(self):
        super().__init__('чёрный')

    def question(self):
        x, y = super().question()
        self.__quest = f'{x} * {y}'
        self.set_answer(x * y)
        return self.__quest

enemy_types = [GreenDragon, RedDragon, BlackDragon]
