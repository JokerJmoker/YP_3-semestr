# coding: utf-8
# license: GPLv3


class Attacker:
    def __init__(self, health, attack):
        self._health = health
        self._attack = attack
        
    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        return self._health > 0
    