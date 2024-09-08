# coding: utf-8
# license: GPLv3

class Attacker:
    def __init__(self, health, attack):
        self._health = health
        self._attack = attack
        
    def attack(self, target):
        target._health -= self._attack
        print(f'Нанесено {self._attack} урона! У {target._color} дракона осталось {target._health} здоровья.')

    def is_alive(self):
        return self._health > 0
