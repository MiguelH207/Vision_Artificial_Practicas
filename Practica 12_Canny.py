import numpy as np 
import cv2
from matplotlib import pyplot as plt 


img=cv2.imread("imagen2.jpg", cv2. IMREAD_GRAYSCALE)
assert img is not None,"No hay Lectura de imagen"
edges = cv2. Canny(img, 100, 200)

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Imagen original'), plt.xticks([]),plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray') 
plt.title('Imagen bordeada'), plt.xticks([]),plt.yticks([])
plt.show()
cv2.imwrite("Bordes.jpg", edges)
cv2.imshow("Bordes", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()