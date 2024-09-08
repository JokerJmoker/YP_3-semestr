# coding: utf-8
# license: GPLv3
from gameunit import *


class Hero(Attacker):
    def __init__(self, name):
        super().__init__(health=100, attack=50)  
        self._name = name
        self._experience = 0
        
    
    def attack(self, target):
        super().attack(target)
        
            
    
