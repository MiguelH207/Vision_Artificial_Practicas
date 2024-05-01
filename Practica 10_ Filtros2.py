# Miguel Angel Huerta Castillo      21310236
# Practica X: Filtros II
 

import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('imagen2.jpg', 0)

# Aplicar el algoritmo de Canny para detección de bordes
bordes = cv2.Canny(imagen, 100, 200)  # Umbral mínimo y máximo

# Mostrar la imagen original y los bordes detectados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Bordes Detectados', bordes)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
