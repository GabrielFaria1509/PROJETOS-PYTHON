import cv2 as cv   ##puxa biblioteca OpenCV

webcam = cv.VideoCapture(0)    ## 0 = webcam padrão do computador

if webcam.isOpened() :
   validacao , frame = webcam.read()  ## lê a imagem da webcam
   while validacao:         ## enquanto a webcam estiver aberta
       validacao, frame = webcam.read()
       cv.imshow("Webcam", frame)          ## mostra a imagem da webcam
       key = cv.waitKey(10)        ## espera 10ms para ler a tecla pressionada
       if key == 27:
           break   ## se a tecla pressionada for ESC, sai do loop
cv.imwrite("imagem.jpg", frame)  ## salva a imagem capturada 

webcam.release()   ## libera a webcam
cv.destroyAllWindows()  ## fecha todas as janelas abertas
       
