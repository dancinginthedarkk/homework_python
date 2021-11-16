import numpy as np

def add_matrix(list_1, list_2):
    return np.add(list_1, list_2)

def multiplication(list_1, list_2):
    return np.dot(list_1, list_2)

def transposition(list_1):
    matrix = np.transpose(list_1)
    return(matrix)

list1 = [[1, 1, 1],
         [2, 2, 2],
         [3, 3, 3]]
list2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(add_matrix(list1, list2))
print()
print(multiplication(list1, list2))
print()
print(transposition(list1))