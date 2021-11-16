###       TP7_Transformación Afín con Eventos del mouse       ###
###                                                           ###
### NOTA: Se cargan 2 imagenes:                               ###
###   (a o A) Habilita la selección de 3 puntos con el mouse, ###
###   (g o G) Guarda la imagen nueva con el incruste,         ###
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
print('--- Presione A, seleccione 3 puntos y luego presione G para guardar.\n --- Si desea, presione Q para salir.')

def trans_afin(image, origen, destino):                     #Recibe los 3 puntos para la transformación
    (al, an) = image.shape[:2]

    M = cv2.getAffineTransform(origen, destino)         #Matriz transf afin

    img_out = cv2.warpAffine(image, M, (al,an))         #Transformacion afin
                                                        
    return img_out

def dibuja (event, x, y, flags, param):           #Función que grafica el rectángulo
    global x1, y1, x2, y2, x3, y3, count               
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
            count = 0


image = cv2.imread('escenario.jpg')                         #Imagen de fondo
(h, w) = image.shape[:2]                                

img_incr = cv2.imread('perrito.jpg')                         #Imagen de incruste
(H, W) = img_incr.shape[:2]


img_out = np.zeros((h,w), np.uint8)                         #Imagen de salida

while True: 
    cv2.imshow('Imagen de fondo', image) #Muestro imagen de fondo
    k = cv2.waitKey(1) & 0xFF

    if k == (ord ('q') or ord('Q') or 27):                                   #Sale al presionar 'q'
        break

    if k == (ord('a') or ord('A')):                                   #Selecciona tres puntos con 'a'

        cv2.namedWindow('Imagen de fondo')
        cv2.setMouseCallback('Imagen de fondo', dibuja)     #Cuando hay un evento del mouse se llama a f
    
    if k == (ord('g') or ord('G')):                                   #Guardo al presionar 'g'
        origen = np.float32([[0,0],[W-1,0],[0,H-1]])    #3 vertices de la imagen a incrustar
        destino = np.float32([[x1,y1],[x2,y2],[x3,y3]]) #Puntos seleccionados en el fondo
        img_incr = trans_afin(img_incr,origen,destino)          #Transformación afin del incruste

        mascara = np.array([[x1,y1],[x3,y3],[x3+x2-x1,y3+y2-y1],[x2,y2]],np.int32)  #Mascara para sumar imagenes
        cv2.fillPoly(image, [mascara], (0,0,0), cv2.LINE_AA)                        #Aplico máscara al fondo

        img_incr = img_incr[0:h, 0:w]                   #(Si img_incr es mas chica, tira error... )
        img_out = cv2.add(image,img_incr)                 #Sumo imágen del fondo con la incrustada.
        cv2.imwrite('output.jpg',img_out)               #Guardo la imagen de salida
        break 

cv2.imshow('Imagen de salida', img_out) 
cv2.waitKey(0)

cv2.destroyAllWindows()                                 
