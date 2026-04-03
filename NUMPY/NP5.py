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

array2 = kp.arange(1, 7)
print(array2)
array3 = array2.reshape(2, 3)
print(array3)
print(array3.flatten())

array4 = kp.array([[1, 2, 3], [4, 5, 6]])

print(array4.shape)
print(array4.ndim)
print(array4.size)
print(array4.dtype)
