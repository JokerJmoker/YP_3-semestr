import pickle
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data.pickle')

try:
    with open(file_path, 'rb') as f:
        deserialized_objects = pickle.load(f)

    iterator, some_function, library_class = deserialized_objects

    try:
        # Проверка работы с итератором
        print(list(iterator))
    except Exception as e:
        print(f"Error with iterator: {e}")

    try:
        # Проверка работы с встроенной функцией
        print(some_function(-10))
    except Exception as e:
        print(f"Error with builtin_function: {e}")

    try:
        # Проверка работы с классом из библиотеки
        print(library_class([1, 2, 3]))
    except Exception as e:
        print(f"Error with library_class: {e}")

except FileNotFoundError:
    print(f"File not found: {file_path}")
