import cv2 as cv   ##puxa biblioteca OpenCV
from datetime import datetime as dt  ##puxa biblioteca datetime

webcam = cv.VideoCapture(0)    ## 0 = webcam padrão do computador
## mostrar cobrindo tela toda 
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 1920)  ## largura da imagem
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 720)  ## altura da imagem

fps = webcam.set(cv.CAP_PROP_FPS, 30)  ## frames por segundo

if webcam.isOpened():
    validacao, frame = webcam.read()  ## lê a imagem da webcam
    while validacao:  ## enquanto a webcam estiver aberta
        validacao, frame = webcam.read()

        data = dt.now()  ## pega a data e hora atual
        exibicao = data.strftime("%d-%m-%Y %H:%M:%S")  ## formata a data e hora

        # Mensagens ajustadas
        #primeiro parenteses é a posição do texto(x,y)
        #primero num isolada é a escala , segundo é a espessura
        #parenteses com 3 núemeros é a cor (B,G,R) ,RGB o quanto tem de azul verde e vermelho
        cv.putText(frame, "Sorria!", (30, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.putText(frame, "Pressione ESC para sair", (30, 90), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.putText(frame, exibicao, (30, 130), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.putText(frame, f"Frame por segundo: {int(webcam.get(cv.CAP_PROP_FPS))}", (30, 170),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv.imshow("Webcam", frame)  ## mostra a imagem da webcam
        key = cv.waitKey(10)  ## espera 10ms para ler a tecla pressionada

        if key == 27:
            break  ## se a tecla pressionada for ESC, sai do loop

cv.imwrite("PrintWebcam.jpg", frame)  ## salva a imagem capturada
webcam.release()  ## libera a webcam
cv.destroyAllWindows()  ## fecha todas as janelas abertas
