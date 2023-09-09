import numpy as np
array_1 = np.random.randint(1 ,20, size=(4, 3))
array_2 = np.zeros(shape=(array_1.shape[1], array_1.shape[0]))
for i in range(array_1.shape[0]):
    for j in range(array_1.shape[1]):
        array_2[j,i] = array_1[i, j]
print(array_1)
print(array_2)