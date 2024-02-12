import numpy as np
import sympy as sp

x = sp.symbols('x')

# matriisit
matrix_a = np.array([[4, 9, 0], [-3, 7, -11]])
matrix_b = np.array([[8, 9], [-3, 12], [0, -1], [7, 1]])

# transpoosit
transp_a = matrix_a.T
transp_b = matrix_b.T

# matriisi 3.1.
matrix = np.array([[-2, 0, 8, 5], [3, -1, 2, 1], [4, 7, 6, 2], [1, 0, 2, 3]])

# 2.1. a) determinantti
matrix_a1 = np.array([[5, -6], [8, 10]])
det_a1 = np.linalg.det(matrix_a1)

# 2.1 b) determinantti
matrix_b1 = sp.Matrix([[1-x, -x], [x, 1-x]])
det_b1 = matrix_b1.det()

# 2.2. a) determinantti
matrix_a2 = np.array([[2, 3, 4], [-2, -1, 1], [5, 3, 2]])
det_a2 = np.linalg.det(matrix_a2)

# 2.2. b) determinantti
matrix_b2 = np.array([[3, 15, 7], [0, -4, 0], [3, 2, 3]])
det_b2 = np.linalg.det(matrix_b2)

# 3.1. determinantti
determinant = np.linalg.det(matrix)

print("A:n transpoosi:")
print(transp_a)
print("B:n transpoosi:")
print(transp_b)

print("2.1 a) determinantti:")
print(f"{det_a1:.2g}")
print("2.1 b) determinantti:")
print(f"{det_b1}")
print("2.2 a) determinantti:")
print(f"{det_a2:.2g}")
print("2.2 b) determinantti:")
print(f"{det_b2:.2g}")
print("3.1 determinantti:")
print(f"{determinant:.3g}")
