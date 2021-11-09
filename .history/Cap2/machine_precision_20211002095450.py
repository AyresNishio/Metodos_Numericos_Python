import numpy as np

#Precisão Máquina Pyhon (Biblioteca Numpy)
print("Float:\n")
print(np.finfo(float).eps)

print("Float 32 bits:\n")
print(np.finfo(np.float32).eps)

print("Float 64 bits:\n")
print(np.finfo(np.float64).eps)

print("Float 128 bits:\n")
print(np.finfo(np.float128).eps)


#Precisão Máquina Algoritmo
 