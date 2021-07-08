#! /usr/bin/env python
# -*- coding: utf-8 -*-

### TP3_Cálculo de alto y ancho de una captura (webcam)  ###
### para no harcodear                                    ###
### Alumno: HABIAGUE, Carlos.                            ###
###                                                      ###
###--""VISIÓN POR COMPUTADORA" 2021--                    ###
import cv2
#from skimage import io


cap = cv2.VideoCapture (0)
#leido, frames = cap.read() #Utilizo la cámara para sacar una foto de prueba. Es a la que le voy a medir sus parámetros (alto, ancho y canales).
#grays = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
#if leido == True:
#	cv2.imwrite("foto_prueba.png", grays)
#	print("Foto de prueba tomada correctamente")
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


#(alto, ancho, canales) = frames.shape # Acá consigo los valores con la función shape.
print('El alto de la imágen es: {} y el ancho es: {}'.format(height, width))


fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (height,width)) #Acá indexo automáticamente los valores de ancho y alto de la imágen. 
while (cap.isOpened ()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret is True:
        out.write(gray)
        cv2.imshow('frame', gray )
        if cv2.waitKey(1) & 0xFF == ord ('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
