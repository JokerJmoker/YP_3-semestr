class Animal:
    def __init__(self, name, age ) -> None: 
        self.name = str(name)
        self.age = int(age)


class Dolpin(Animal): # наследование
    def __init__(self, name, age, friends):
        super().__init__(name, age)
        self._friends = str(friends) # инкапсуляция

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, friends: {self._friends}"
    
class Zebra(Animal): # наследование 
    def __init__(self, name, age, enemies):
        super().__init__(name, age)
        self._enemies = str(enemies) # инкапсуляция 

    def __str__(self): # полиморфизм 
        return f"name: {self.name}, age: {self.age}, enemies: {self._enemies}" 

dolphin = Dolpin("Joseph", 8,"leopard and Joker" )
zebra = Zebra("Adolph ", 7 ,"leopard and Joker" )

print(dolphin)
print(zebra)