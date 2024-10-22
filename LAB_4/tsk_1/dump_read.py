import pickle

with open('data.pickle', 'rb') as f:
    deserialized_objects = pickle.load(f)

iterator, some_function, library_class = deserialized_objects

try:
    # проверка работы с итератором
    print(list(iterator))
except Exception as e:
    print(f"Error with iterator: {e}")

try:
    # проверка работы сo встроенной функцией
    print(some_function(-10))
except Exception as e:
    print(f"Error with builtin_function: {e}")

try:
    # проверка работы с классом из библиотеки
    print(library_class([1, 2, 3]))
except Exception as e:
    print(f"Error with library_class: {e}")
