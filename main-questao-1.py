import cv2
import numpy as np

imagem = cv2.imread("Marrie.jpeg")

if imagem is None:
    print("Imagem não encontrada")
else:
    print("Tem imagem")
    print("")

    altura, largura, canais = imagem.shape
    tipo = imagem.dtype

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    cinza_maximo = np.max(imagem_cinza)
    cinza_medio  = np.mean(imagem_cinza)
    cinza_minimo = np.min(imagem_cinza)

    print(f"altura: {altura}")
    print(f"largura: {largura}")
    print(f"canais de cor: {canais}")
    print(f"tipo de dado: {tipo}")
    print(f"tom de cinza maximo: {cinza_maximo}")
    print(f"tom de cinza medio: {cinza_medio}")
    print(f"tom de cinza minimo: {cinza_minimo}")


