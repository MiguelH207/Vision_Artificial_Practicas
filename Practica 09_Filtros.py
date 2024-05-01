import cv2
import numpy as np

# Función para agregar ruido gaussiano a una imagen
def agregar_ruido_gaussiano(imagen):
    filas, columnas, canales = imagen.shape
    media = 0
    varianza = 0.1
    sigma = varianza ** 0.5
    ruido = np.random.normal(media, sigma, (filas, columnas, canales))
    ruido = ruido.reshape(filas, columnas, canales)
    ruidosa = imagen + ruido
    return np.clip(ruidosa, 0, 255).astype(np.uint8)

# Función para agregar ruido Sal y Pimienta a una imagen
def agregar_ruido_sal_pimienta(imagen, cantidad=0.05):
    filas, columnas, _ = imagen.shape
    num_sal = np.ceil(cantidad * imagen.size * 0.5)
    num_pimienta = np.ceil(cantidad * imagen.size * 0.5)
    
    # Sal
    coords_sal = [np.random.randint(0, i - 1, int(num_sal)) for i in imagen.shape]
    imagen[coords_sal[0], coords_sal[1], :] = 255

    # Pimienta
    coords_pimienta = [np.random.randint(0, i - 1, int(num_pimienta)) for i in imagen.shape]
    imagen[coords_pimienta[0], coords_pimienta[1], :] = 0
    return imagen

# Funciones para aplicar diferentes filtros a una imagen
def aplicar_filtro_gaussiano(imagen):
    return cv2.GaussianBlur(imagen, (5, 5), 0)

def aplicar_filtro_media(imagen):
    return cv2.blur(imagen, (5, 5))

def aplicar_filtro_mediana(imagen):
    return cv2.medianBlur(imagen, 5)

def aplicar_filtro_minimo(imagen):
    return cv2.erode(imagen, np.ones((5, 5), np.uint8))

def aplicar_filtro_maximo(imagen):
    return cv2.dilate(imagen, np.ones((5, 5), np.uint8))

# Cargar la imagen de entrada
ruta_imagen = "imagen2.jpg"  # Ruta de tu imagen
imagen = cv2.imread(ruta_imagen)

# Agregar ruido gaussiano
imagen_con_ruido_gaussiano = agregar_ruido_gaussiano(imagen.copy())

# Agregar ruido Sal y Pimienta
imagen_con_ruido_sal_pimienta = agregar_ruido_sal_pimienta(imagen.copy())

# Mostrar las imágenes antes de guardarlas
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen con Ruido Gaussiano", imagen_con_ruido_gaussiano)
cv2.imshow("Imagen con Ruido Sal y Pimienta", imagen_con_ruido_sal_pimienta)

# Esperar a que el usuario presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aplicar diferentes filtros a las imágenes contaminadas
imagenes_filtradas_gaussiano = {
    "Gaussiano": aplicar_filtro_gaussiano(imagen_con_ruido_gaussiano),
    "Media": aplicar_filtro_media(imagen_con_ruido_gaussiano),
    "Mediana": aplicar_filtro_mediana(imagen_con_ruido_gaussiano),
    "Mínimo": aplicar_filtro_minimo(imagen_con_ruido_gaussiano),
    "Máximo": aplicar_filtro_maximo(imagen_con_ruido_gaussiano)
}

imagenes_filtradas_sal_pimienta = {
    "Gaussiano": aplicar_filtro_gaussiano(imagen_con_ruido_sal_pimienta),
    "Media": aplicar_filtro_media(imagen_con_ruido_sal_pimienta),
    "Mediana": aplicar_filtro_mediana(imagen_con_ruido_sal_pimienta),
    "Mínimo": aplicar_filtro_minimo(imagen_con_ruido_sal_pimienta),
    "Máximo": aplicar_filtro_maximo(imagen_con_ruido_sal_pimienta)
}

# Mostrar imágenes filtradas individualmente
for nombre_filtro, imagen_filtrada in imagenes_filtradas_gaussiano.items():
    cv2.imshow(f"Filtro Gaussiano: {nombre_filtro}", imagen_filtrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for nombre_filtro, imagen_filtrada in imagenes_filtradas_sal_pimienta.items():
    cv2.imshow(f"Filtro Sal y Pimienta: {nombre_filtro}", imagen_filtrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Guardar las imágenes resultantes
cv2.imwrite("imagen_con_ruido_gaussiano.jpg", imagen_con_ruido_gaussiano)
cv2.imwrite("imagen_con_ruido_sal_pimienta.jpg", imagen_con_ruido_sal_pimienta)

for nombre_filtro, imagen_filtrada in imagenes_filtradas_gaussiano.items():
    cv2.imwrite(f"imagen_filtrada_gaussiano_{nombre_filtro}.jpg", imagen_filtrada)

for nombre_filtro, imagen_filtrada in imagenes_filtradas_sal_pimienta.items():
    cv2.imwrite(f"imagen_filtrada_sal_pimienta_{nombre_filtro}.jpg", imagen_filtrada)

print("Proceso completado. Imágenes guardadas.")
