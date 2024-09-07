class Mother:
    def __init__(self, age, hair_color): # инкапсуляция 
        self._age = int(age)
        self._hair_color = str(hair_color)

    def __str__(self):
        return f"Mother's age is {self._age} , Mother's hair color is {self._hair_color}"
    
class Daughter(Mother): # наследование 
    def __init__(self, age, hair_color, eye_color):
        super().__init__(age, hair_color) # расширеник конструктора __init__ посредством добавления скрытой переменной eye_color
        self._eye_color = eye_color 

    def __str__(self): # полиморфизм (одинаковые методы __str__ имеют отличную реализацию в соответсвующих классах )
       return f"Daughter's age is {self._age}, Daughter's hair color is {self._hair_color}, Daughter's eye color is {self._eye_color}"
 
mother = Mother(25, "white")
daughter = Daughter(11, "black", "green")
        
print(mother)
print(daughter)
        