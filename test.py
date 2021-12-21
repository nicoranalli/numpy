import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1,2,3],[1,2,3]])
print(a)
print('Shape:', a.shape)
print('Size:', a.size)
print('Bytes:', a.nbytes)

print('\nArange function')
b = np.arange(0,10,2)
print(b)

print('\nArray random permutation')
c= np.random.permutation(b)
print(c)

d = np.random.rand(100)
print(d)

plt.hist(d)
plt.show()