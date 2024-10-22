import pickle
from collections import deque

# Объекты
iterator = iter([1, 2, 3, 4, 5])
some_function = abs
library_class = deque

# Список для сериализации
objects = [iterator, some_function, library_class]

with open('data.pickle', 'wb') as f:
    pickle.dump(objects, f)