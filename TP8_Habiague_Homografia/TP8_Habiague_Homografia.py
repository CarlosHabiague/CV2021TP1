###     TP8_Homografía_Rectificación conEventos del mouse     ###
###                                                           ###
### NOTA: Se carga una imágen y luego:                        ###
###   (h o H) Habilita la selección de 4 puntos con el mouse, ###
###   (g o G) Guarda la imagen nueva rectificada,             ###
###   (q o Q o ESCAPE) salir                                  ###
###                                                           ###
### Alumno: HABIAGUE, Carlos.                                 ###
###                                                           ###
###             --"VISIÓN POR COMPUTADORA" 2021--             ###



#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

blue = (255, 0, 0); green = (0, 255, 0); red = (0, 0, 255);     #Define colores

count = 1                                              

print('---------- TRANSFORMACIONES DE IMÁGENES CON OPEN CV ---------- \n\n')
print('--- Presione H, seleccione 4 puntos y luego presione G para guardar.\n --- Si desea, presione Q para salir.')

def homo(image, origen, destino):                     #Recibe los 3 puntos para la homografía
    (al, an) = image.shape[:2]

    M = cv2.getPerspectiveTransform(origen, destino)         #Matriz de homografía

    img_out = cv2.warpPerspective(image, M, (al,an))         #Transformación afin
                                                        
    return img_out

def dibuja (event, x, y, flags, param):           #Función que define la selección
    global x1, y1, x2, y2, x3, y3, x4, y4, count               
    if event == cv2.EVENT_LBUTTONDOWN:                  
        if count == 1:
            x1, y1 = x, y                               #Guardo el punto 1
            cv2.circle(image, (x,y),2,green,-1)           
            count = 2
        elif count == 2:
            x2, y2 = x, y                               #Guardo el punto 2
            cv2.circle(image, (x,y),2,green,-1)          
            count = 3
        elif count == 3:
            x3, y3 = x, y                               #Guardo el punto 3
            cv2.circle(image, (x,y),2,green,-1)         
            count = 4
        elif count == 4:
            x4, y4 = x, y                               #Guardo el punto 4
            cv2.circle(image, (x,y),2,green,-1)         
            count = 0


image = cv2.imread('pc.jpg')                         #Imágen 
(h, w) = image.shape[:2]                                


while True: 
    cv2.imshow('Imagen a rectificar', image)                #Muestro imaágen de fondo
    k = cv2.waitKey(1) & 0xFF

    if k == (ord ('q') or ord('Q') or 27):                  #Sale al presionar 'Q'
        break

    if k == (ord('h') or ord('H')):                         #Selecciona 4 puntos con 'H'

        cv2.namedWindow('Imagen a rectificar')
        cv2.setMouseCallback('Imagen a rectificar', dibuja)

    
    if k == (ord('g') or ord('G')):                                   #Guardo al presionar 'G'
        destino = np.float32([[0,0],[w-1,0],[0,h-1],[w-1,h-1]])       #Aquí están los 4 vertices de la imágen 
        origen = np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])        #Puntos determinados 
        
        img_out = homo(image,origen,destino)      #Transformo 
        img_out = img_out[0:h, 0:w]

        cv2.imwrite('output.jpg', img_out)        #Guardo 
        break 

cv2.imshow('Imagen de salida', img_out) 
cv2.waitKey(0)

cv2.destroyAllWindows() 
