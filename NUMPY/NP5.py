import numpy as kp

array = kp.array([66, 88, 55, 99, 33])
print(array[1:2])
print(array[1:])
print(array[:5])
print(array[4:5])
print(array[3:5])

array1 = kp.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
print(array1[1:2, 2:4])
