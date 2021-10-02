import numpy as np

#Precisão Máquina Pyhon (Biblioteca Numpy)
print("Float:\n")
print(np.finfo(float).eps)

print("Float:\n")
print(np.finfo(np.float32).eps)

print("Float:\n")
print(np.finfo(np.float64).eps)

print("Float:\n")
print(np.finfo(np.float128).eps)


#Precisão Máquina Algoritmo
#  