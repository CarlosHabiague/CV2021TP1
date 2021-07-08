###    TP5_Transformación Euclidiana con Eventos del mouse    ###
###                                                           ###
### NOTA: Se carga una imágen, se selecciona el recorte       ###
###       y con la entrada por teclado se opta por:           ###
###       (e o E) Aplica transformación, guarda y sale.       ###
###       (r o R) Vuelve a seleccionar el recote,             ###
###       (q o Q o ESCAPE) salir                              ###
###IMPORTANTE: El programa sólo acepta el evento de mouse     ###
###            iniciando desde la esquina superior izquierda  ###
###            hacia el final en la esquina inferior derecha. ###
### Alumno: HABIAGUE, Carlos.                                 ###
###                                                           ###
###             --"VISIÓN POR COMPUTADORA" 2021--             ###



#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math

blue = (255, 0, 0 ); green = (0, 255, 0); red = (0, 0, 255)
capturing = False
# true si el botón está presionado
mode = False
k = 0
xybutton_down = -1, -1
tx = 0 
ty = 0
center = None
scale = 1.0
angle = 0


img = cv2.imread('hoja.png')
print('---------- TRANSFORMACIONES DE IMÁGENES CON OPEN CV ---------- \n\n')
print('Seleccione sobre la imágen un recorte:')

def dibuja (event, x, y, flags, param): # param=grosor (si es -1, es relleno)
    global xybutton_down, capturing, mode, imag, x_1, x_2, y_1, y_2, imagen

    if event == cv2.EVENT_LBUTTONDOWN:
        capturing = True
        xybutton_down = x, y
        x_1= x
        y_1= y
    elif event == cv2.EVENT_MOUSEMOVE:
        if capturing is True:
            x_2= x
            y_2= y
            img [ : ] = cv2.imread('hoja.png')
            cv2.rectangle(img, xybutton_down, (x, y), blue, 1)
              
    elif event == cv2.EVENT_LBUTTONUP: # cuando se suelta el clik...
        print('Recorte capturado, presione (e) si desea transformar, guardar y salir, (r) si desea volver a elegir recorte o (q) para salir: ')
        crop_img = img[y_1:y_2, x_1:x_2] #dimensiono mi recorte dentro de la imagen original
        cv2.imshow("cropped", crop_img)
        imagen = crop_img    
        capturing = False
        
cv2.namedWindow('image')
cv2.setMouseCallback ('image', dibuja)
    

def eucl (imagen, angle, tx, ty):
    global imagen_2, shifted, center, scale
    (h, w) = (imagen.shape[0], imagen.shape[1])

    #hipotenusa = math.sqrt((h**2)+(w**2))
    #coseno = math.cos(math.radians(angle))
    #mseno = math.sin(math.radians(angle)) * (-1)
    #seno = math.sin(math.radians(angle))

    N = cv2.getRotationMatrix2D(center, angle, scale)
    M = np.float32([[N[0,0],N[0,1],tx],[N[1,0],N[1,1],ty]])
  
    if center is None :
        center = (w/2, h/2)
    shifted =cv2.warpAffine(imagen, M,(w,h))
    return shifted
    
while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
   
    if k == (ord('e') or ord('E')): # Transforma y guarda la imágen nueva.
        
        tx = input('Ingrese el valor de desplazamiento en X (en pixels): ')
        tx = int(tx)
        ty = input('Ingrese el valor de desplazamiento en Y (en pixels): ')
        ty = int(ty)
        angle = input('Ingrese un valor de ángulo: ')
        angle = int(angle)
        imagen_2 = eucl (imagen, angle, tx, ty)
        cv2.imwrite ('trans_eucl.png', imagen_2)

        print('Seleccion guardada exitosamente con el nombre: trans_eucl.png \n')
        cv2.waitKey(1)
        break

    elif k == (ord('r') or ord('R')): # vuelve a elegir el rectángulo de recorte
        img [:] = cv2.imread('hoja.png')
        mode == 'r'
        print('Seleccione nuevamente la sección que desea:  \n')

    elif k ==  (ord ('q') or ord('Q') or 27): # con q, Q o tecla "escape" sale del programa.
        break
cv2.destroyAllWindows()
