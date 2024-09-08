# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""

class Hero(Attacker):
    def __init__(self, name):
        super().__init__(health=100, attack=50)  
        self._name = name
        self._experience = 0
        
    
    def attack(self, target):
        super().attack(target)
        print(f'{self._name} атакует {target._color} дракона и наносит {self._attack} урона!')
        if not target.is_alive():
            self._experience += 10  
            print(f'{self._name} победил дракона и получил 10 опыта!')
    
