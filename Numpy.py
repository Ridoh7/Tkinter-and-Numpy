import numpy as np

ar1d= np.array([1,2,3,4])

print(ar1d)

ar2d= np.array([[1,2,3,4], [1,2,3,4]])

print(ar2d)

ar3d=np.array([[[1,2,3],
                [1,2,3],
                [1,2,5]]])

print(ar3d)

ar3d=np.add(ar3d, 5)
print(ar3d)

print(np.multiply(ar3d,2))
print(np.sqrt(ar3d))
print(np.divide(ar3d, 4))

array= np.zeros((4,3,2))
print(array)

a=np.arange(0,101,3)
print(a)

array1= np.array([[[1,2,3],
                   [4,5,6],
                   [7,8,9]]])

array2=np.array([[[1,2,3],
                  [4,5,6],
                  [7,8,9]]])

print(np.add(array1,array2))
print(array1.shape)
print(array2.size)