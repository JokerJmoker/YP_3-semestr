import pickle
from collections import deque

iterator = iter([1, 2, 3, 4, 5])
some_function = abs
library_class = deque

objects = [iterator, some_function, library_class] # список для сериализации

with open('data.pickle', 'wb') as f:
    pickle.dump(objects, f)