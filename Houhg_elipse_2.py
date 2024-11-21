import cv2
import numpy as np
import matplotlib.pyplot as plt

# Caminho da imagem
image_path = "C:/python_codigos/Trabalho-1/img/18.jpg"

# Carregar a imagem
image = cv2.imread(image_path, cv2.IMREAD_COLOR)
if image is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
    exit()

# Criar uma cópia da imagem original para preservar a original
image_with_circles = image.copy()

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar um filtro de suavização para reduzir ruído
blurred_image = cv2.GaussianBlur(gray_image, (7, 7), 0)

# Detectar bordas usando o Canny
edges = cv2.Canny(blurred_image, 150, 150)

# Aplicar a Transformada de Hough para detectar elipses
circles = cv2.HoughCircles(
    edges, 
    cv2.HOUGH_GRADIENT, 
    dp=1, 
    minDist=500,
    param1=500,
    param2=30,
    minRadius=20,
    maxRadius=100
)

# Desenhar as elipses detectadas na cópia da imagem original
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])  # Centro da elipse
        radius = circle[2]              # Raio detectado
        # Desenhar o contorno da elipse
        cv2.ellipse(image_with_circles, center, (int(radius * 1.4), int(radius * 0.8)), 180, 0, 360, (100, 255, 0), 2)
        # Desenhar o centro da elipse
        cv2.circle(image_with_circles, center, 5, (0, 0, 255), -1)

# Concatenar as imagens lado a lado
image_combined = np.hstack((image, image_with_circles))

# Converter BGR para RGB (necessário para exibir corretamente no matplotlib)
image_combined = cv2.cvtColor(image_combined, cv2.COLOR_BGR2RGB)

# Exibir a imagem usando matplotlib
plt.figure("Imagem Original e Elipses Detectadas")
plt.imshow(image_combined)
plt.axis("off")

# Habilitar barra de ferramentas para salvar
plt.subplots_adjust(bottom=0.1)  # Ajustar espaço para o botão
plt.show()
