import numpy as np 

# ejercicios de indexacion y slicing 

array = np.array([30, 10, 40, 50, 60])

print("Ultima posicion : ", array[-1])

#imprimir por rango
print("por rango : ", array[2:4])

#Boolean 

print(array >40)

# array con index

index = [1,2,3,]

#imprimir con index 

print(array[index])
