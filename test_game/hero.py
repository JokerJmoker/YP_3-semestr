# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    def __init__(self, name):
        # Инициализация с фиксированными значениями здоровья, атаки и опыта
        super().__init__(health=100, attack=50)  # передаем здоровье и атаку в конструктор Attacker
        self._name = name
        self._experience = 0  # опыт героя начинается с 0
        
    def attack(self, target):
        super().attack(target)  # Используем метод атаки родительского класса
        print(f'{self._name} атакует {target._color} дракона и наносит {self._attack} урона!')
        if not target.is_alive():
            self._experience += 10  # герой получает опыт за победу
            print(f'{self._name} победил дракона и получил 10 опыта!')

    def get_status(self):
        """Выводит текущий статус героя: здоровье и опыт."""
        return f"Герой: {self._name}, Здоровье: {self._health}, Опыт: {self._experience}"
