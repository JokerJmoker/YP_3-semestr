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


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
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
        x,y = super().question()
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
    

class RedDragon(Dragon):
    def __init__(self):
        super().__init__('красный')

    def question(self):
        x,y = super().question()
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
    
    
class BlackDragon(Dragon):
    def __init__(self):
        super().__init__('черный')

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Trolle(Enemy):
    def __init__(self, size):
        super().__init__(health=None, attack=None) 
        self._size = size
        self.__answer = None
        self.__quest = None
        
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
    
    def question(self):
        x = randint(1, 100)
        return x
 

class SmallTrolle(Trolle):
    def __init__(self):
        super().__init__('маленький' , health = 50, attack = 10)

    def question(self):
        x = randint(1, 5)
        self.__quest = str('Какое число от 1 до 5 я загадал?')
        self.set_answer(x)
        return self.__quest


class OrdinaryTroll(Trolle):
    def __init__(self):
        super().__init__('обычный', health = 100, attack = 30)

    def __factorize(n):
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
        return factors

    def question(self):
        x = super().question()
        factors = self.__factorize(x)
        self.__quest = 'Разложи число ' ,str(x), 'на множители и перечисли мне их в порядке возрастания'
        self.set_answer(factors)
        return self.__quest
     

class BigTroll(Trolle):
    def __init__(self):
        super().__init__('большой', health = 200, attack = 50)


    def __is_prime(n):
    
        if n <= 1:
            return 'Нет'
        if n <= 3:
            return 'Да'
        if n % 2 == 0 or n % 3 == 0:
            return 'Нет'
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return 'Нет'
            i += 6
        return 'Да'
    
    def question(self):
        x = super().question()
        ans = self.__is_prime(x)
        self.__quest = 'Является ли число' ,str(x), 'простым? Да или Нет?'
        self.set_answer(ans)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon, SmallTrolle, OrdinaryTroll, BigTroll]