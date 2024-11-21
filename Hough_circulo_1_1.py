import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem
img_path = "C:/python_codigos/Trabalho-1/img/9.jpg"
img = cv2.imread(img_path)

# Converte para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplica filtro Gaussiano para reduzir ruído
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplica filtro Canny para detectar bordas
canny = cv2.Canny(blurred, 10, 150)

# Inverte a imagem
canny = 255 - canny

# Detecta círculos
circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1.0, 500,
                           param1=200, param2=80, minRadius=50, maxRadius=120)

# Copia a imagem original para desenhar os círculos
img_with_circles = img.copy()

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img_with_circles, (x, y), r, (0, 0, 255), 5)
        cv2.circle(img_with_circles, (x, y), 2, (0, 255, 0), 10)

# Configuração do matplotlib
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Remove espaço entre as imagens
plt.subplots_adjust(wspace=0)

# Exibe as imagens
ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax1.axis("off")

ax2.imshow(cv2.cvtColor(img_with_circles, cv2.COLOR_BGR2RGB))
ax2.axis("off")

plt.show()
