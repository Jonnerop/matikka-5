import numpy as np

# a) kertolasku
a1 = np.array([[-1, 2], [3, 1]])
a2 = np.array([[0, 1, 3], [2, -3, 5]])
result_a = np.dot(a1, a2)

# b) kertolasku
b1 = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
b2 = np.array([[1], [-3], [-1]])
result_b = np.dot(b1, b2)

# c) kertolasku
c1 = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
c2 = np.array([[3], [-5], [7]])
result_c = np.dot(c1, c2)

# d) kertolasku
d1 = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
d2 = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
result_d = np.dot(d1, d2)

print("a) vastaus:")
print(result_a)
print("b) vastaus:")
print(result_b)
print("c) vastaus:")
print(result_c)
print("d) vastaus:")
print(result_d)
