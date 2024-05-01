# Miguel Angel Huerta Castillo      21310236
# Practica VIII: Operaciones Lógicas en imágenes


import cv2
import numpy as np

# Cargar la imagen
imagen2 = cv2.imread('imagen1.jpg')
imagen1 = cv2.imread('imagen2.jpg')

# Cambiar el tamaño de la segunda imagen para que coincida con la primera
imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))

# Convertir las imágenes a escala de grises
gris1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
gris2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

# Operaciones lógicas
and_resultado = cv2.bitwise_and(gris1, gris2)
or_resultado = cv2.bitwise_or(gris1, gris2)
not_resultado = cv2.bitwise_not(gris1)
xor_resultado = cv2.bitwise_xor(gris1, gris2)

# Mostrar las imágenes resultantes
cv2.imshow('AND', and_resultado)
cv2.imshow('OR', or_resultado)
cv2.imshow('NOT', not_resultado)
cv2.imshow('XOR', xor_resultado)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
