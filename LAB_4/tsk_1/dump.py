import pickle
from collections import deque
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data.pickle')

iterator = iter([1, 2, 3, 4, 5])
some_function = abs
library_class = deque

objects = [iterator, some_function, library_class]  # список для сериализации

with open(file_path, 'wb') as f:
    pickle.dump(objects, f)
