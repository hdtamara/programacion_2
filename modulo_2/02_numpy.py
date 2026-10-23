import numpy as np

print(np.__version__)

vector_lista = [1,2,3,4,5]
print(2 * vector_lista)

vector_numpy = np.array(vector_lista)
vector_2 = np.array([2,4,5,6,7])
print(vector_numpy*2)
print(vector_numpy + vector_2)