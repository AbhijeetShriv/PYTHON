import numpy as kp

# ONE DIMENSION
array = kp.array([1, 2, 3, 4])
print(array)
# TWO DIMENSION
array1 = kp.array([[1, 2], [3, 4]])
print(array1[0])
# THREE DIMENSION
array2 = kp.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array2)

# Range
array3 = kp.arange(1, 10)
print(array3)

array4 = kp.arange(1, 32, 4)
print(array4)

array5 = kp.zeros(8)
print(array5)

array6 = kp.zeros((3, 4))
print(array6)

array7 = kp.ones(2)
print(array7)

array8 = kp.ones([3, 4])
print(array8)
