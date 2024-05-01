# Miguel Angel Huerta Castillo      21310236
# Practica VII: Transformaciones en imágenes


import cv2
import numpy as np


# Cargar la imagen
imagen = cv2.imread('imagen.jpg')
# Obtener las dimensiones de la imagen
alto, ancho = imagen.shape[:2]

#### TRASLACION ####
# Definir la matriz de traslación
traslacion_x = 50
traslacion_y = 50
matriz_traslacion = np.float32([[1, 0, traslacion_x], [0, 1, traslacion_y]])
# Aplicar la traslación
imagen_traslacion = cv2.warpAffine(imagen, matriz_traslacion, (ancho, alto))


#### ROTACION ####
# Definir el centro de rotación
centro_rotacion = (ancho // 2, alto // 2)
angulo_rotacion = 45
matriz_rotacion = cv2.getRotationMatrix2D(centro_rotacion, angulo_rotacion, 1)  # Calcular la matriz de rotación
imagen_rotacion = cv2.warpAffine(imagen, matriz_rotacion, (ancho, alto))    # Aplicar la rotación


#### ESCALA ####
# Definir el factor de escala
factor_escala = 0.5
# Redimensionar la imagen
imagen_escala = cv2.resize(imagen, None, fx=factor_escala, fy=factor_escala)


#### RECORTAR ####
# Definir las coordenadas del rectángulo de recorte
x1, y1 = 100, 100
x2, y2 = 300, 300
imagen_recortada = imagen[x1:x2, y1:y2]     # Recortar la imagen


# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Traslacion', imagen_traslacion)
cv2.imshow('Rotacion', imagen_rotacion)
cv2.imshow('Escala', imagen_escala)
cv2.imshow('Recorte', imagen_recortada)


# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
