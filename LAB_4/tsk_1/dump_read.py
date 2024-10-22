import pickle

# Десериализация объектов
with open('data.pickle', 'rb') as f:
    deserialized_objects = pickle.load(f)

iterator, some_function, library_class = deserialized_objects

# Проверяем возможность взаимодействия с объектами
try:
    # Проверка работы с итератором
    print(list(iterator))
except Exception as e:
    print(f"Error with iterator: {e}")

try:
    # Проверка работы сo встроенной функцией
    print(some_function(-10))
except Exception as e:
    print(f"Error with builtin_function: {e}")

try:
    # Проверка работы с классом из библиотеки
    print(library_class([1, 2, 3]))
except Exception as e:
    print(f"Error with library_class: {e}")
