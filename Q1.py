import numpy as np
import numpy.random

arr_1 = numpy.random.randint(1, 10, size=(3, 3))
arr_2 = numpy.transpose(arr_1)
det = np.linalg.det(arr_1)
print(int(det))
inverse = 0
if det:
    inverse = np.linalg.inv(arr_1)

print(arr_1)
print(arr_2)
print(det)
print(inverse)
