import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen2.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro Prewitt
kernel_prewitt_x = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])
kernel_prewitt_y = np.array([[-1, -1, -1],
                             [0, 0, 0],
                             [1, 1, 1]])

prewitt_x = cv2.filter2D(imagen, -1, kernel_prewitt_x)
prewitt_y = cv2.filter2D(imagen, -1, kernel_prewitt_y)
prewitt = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

# Aplicar filtro Sobel
sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)

# Aplicar filtro Roberts
kernel_roberts_x = np.array([[1, 0],
                              [0, -1]])
kernel_roberts_y = np.array([[0, -1],
                              [1, 0]])

roberts_x = cv2.filter2D(imagen, -1, kernel_roberts_x)
roberts_y = cv2.filter2D(imagen, -1, kernel_roberts_y)
roberts = cv2.addWeighted(roberts_x, 0.5, roberts_y, 0.5, 0)

# Mostrar las imágenes resultantes
cv2.imshow('Imagen original', imagen)
cv2.imshow('Filtro Prewitt', prewitt)
cv2.imshow('Filtro Sobel', sobel)
cv2.imshow('Filtro Roberts', roberts)
cv2.waitKey(0)
cv2.destroyAllWindows()
