import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread("Marrie.jpeg")

if imagem is None:
    print("Não tem imagem")
else:
    print("tem imagem")
    print("")
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    media = cv2.blur(imagem_cinza, (5,5))
    mediana = cv2.medianBlur(imagem_cinza, 5)
    gaussiano = cv2.GaussianBlur(imagem_cinza, (5,5), 0)


    plt.figure(figsize=(10,5))
    
    plt.subplot(2, 2, 1)
    plt.imshow(imagem_cinza, cmap='gray')
    plt.title('Imagem Original')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(media, cmap='gray')
    plt.title('Filtro da Média')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(mediana, cmap='gray')
    plt.title('Filtro da Mediana')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(gaussiano, cmap='gray')
    plt.title('Filtro Gaussiano')
    plt.axis('off')

    plt.savefig("Resultados.png")

    plt.show()
    