from binarizacao import Binarizacao
import cv2
import numpy
from PIL import Image
import time

# parametro 0 para webcam integrada / usb
# url para camera ip
camera = cv2.VideoCapture('http://192.168.0.4:8080/video')

while (True):
    time.sleep(2)

    # captura imagem da camera ip
    conectado, img_camera = camera.read()

    # transforma imagem em preta e branca
    img_cinza = cv2.cvtColor(img_camera, cv2.COLOR_BGR2GRAY)

    # diminui tamanho da imagem para 200 x 100
    img_pequena = cv2.resize(img_cinza, (200, 100))

    # converte imagem de CV2 para PIL
    img_plp = Image.fromarray(cv2.cvtColor(img_pequena,cv2.COLOR_BGR2RGB))  

    # binariza a imagem
    img_binarizada = Binarizacao(img_plp, 80).processar()

    # converte imagem de PIL para CV2
    img_mat = cv2.cvtColor(numpy.asarray(img_binarizada), cv2.COLOR_RGB2BGR)

    # aumenta tamanho da imagem para 800 x 600
    img_grande = cv2.resize(img_mat, (800, 600))

    # mostra imagem em tela
    cv2.imshow("binarizacao", img_grande)
    cv2.waitKey(1)