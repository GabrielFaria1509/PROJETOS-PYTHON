import cv2 as cv   ##puxa biblioteca OpenCV

webcam = cv.VideoCapture(0)    ## 0 = webcam padrão do computador
## mostrar cobrindo tela toda 
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 1920)  ## largura da imagem
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 720)  ## altura da imagem


if webcam.isOpened() :
   validacao , frame = webcam.read()  ## lê a imagem da webcam
   while validacao:         ## enquanto a webcam estiver aberta
       validacao, frame = webcam.read()
       
       cv.putText(frame, "Sorria !",(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)## mostra a mensagem na tela
       
       cv.imshow("Webcam", frame)          ## mostra a imagem da webcam
       key = cv.waitKey(10)        ## espera 10ms para ler a tecla pressionada
       
       cv.putText(frame, "Registro salvo",(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)## mostra a mensagem na tela
       
       if key == 27:
           break   ## se a tecla pressionada for ESC, sai do loop
cv.imwrite("PrintWebcam.jpg", frame)  ## salva a imagem capturada 


webcam.release()   ## libera a webcam
cv.destroyAllWindows()  ## fecha todas as janelas abertas
       
