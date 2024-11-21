import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread("C:/python_codigos/Trabalho-1/img/10.png")

# Converte para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplica filtro Gaussiano para reduzir ruído
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Aplica filtro Canny para detectar bordas
canny = cv2.Canny(blurred, 100, 150)

# Inverte a imagem
canny = 255 - canny

# Detecta círculos
circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 3, 250,
                            param1=10, param2=80, minRadius=00, maxRadius=200)

# Desenha os círculos na imagem original
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 0, 255), 5)
        cv2.circle(img, (x, y), 2, (0, 255, 0), 5)

# Exibe as imagens
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()