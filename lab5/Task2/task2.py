import numpy as np

n_x_m = np.random.random((208, 15))
a = np.array([-6, 67, 10, 13 ,-8, 123, 56], int)
z = 53.231


def closest(A, z):
    index = np.abs(A-z).argmin()
    return A[index]

print(n_x_m, "\n Size of my array\n",n_x_m.size)
print("The closest number to ", z, " is ",  closest(a, z), "in array of these numbers ", a)