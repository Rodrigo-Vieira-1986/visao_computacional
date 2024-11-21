import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img_path = 'C:\\python_codigos\\Trabalho-1\\img\\15.jpg'
img = cv2.imread(img_path)

# Converter para escala de cinza e aplicar filtro Gaussiano (códigos originais)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detectar bordas e aplicar a transformada de Hough (códigos originais)
edges = cv2.Canny(blurred, 150, 250)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=100)

# Desenhar as linhas na cópia da imagem original
img_with_lines = img.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_with_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Exibir as imagens lado a lado usando o Matplotlib
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Converter para RGB para o Matplotlib
axs[0].axis('off')
axs[1].imshow(cv2.cvtColor(img_with_lines, cv2.COLOR_BGR2RGB))
axs[1].axis('off')
plt.tight_layout()
plt.show()