### TP3_Cálculo de los FPS de una captura (webcam)       ###
### NOTA: Se realizó de 2 formas diferentes              ###
### Alumno: HABIAGUE, Carlos.                            ###
###                                                      ###
###--"VISIÓN POR COMPUTADORA" 2021--                     ###


#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cv2

captura = cv2.VideoCapture('Naturaleza.avi')
frame_count = 0
all_frames = []
fps = captura.get(cv2.CAP_PROP_FPS)
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    if cv2.waitKey(int(fps)) == ord('q'):
      break
  else: break
  all_frames.append(imagen)
  frame_count = frame_count + 1


print ('Frames por segundo usando video.get(cv2.CAP_PROP_FPS) : {0}'.format(fps))

print ('La cantidad de frames del video es: ' + str(frame_count))
print ('La duración del video de muestra es: 30 segundos.')
print ('Por lo tanto, los FPS calculados del video son: ' + str(frame_count/30))

captura.release()
cv2.destroyAllWindows()
