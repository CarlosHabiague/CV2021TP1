###          TP4_Eventos del mouse y Open CV             ###
### NOTA: Se carga una imágen, se selecciona el recorte  ###
###       y con la entrada por teclado se opta por:      ###
###       (g o G) Guardar y salir,                       ###
###       (r o R) Volver a seleccionar el recote,        ###
###       (q o Q o ESCAPE) salir                         ###
### Alumno: HABIAGUE, Carlos.                            ###
###                                                      ###
###          --"VISIÓN POR COMPUTADORA" 2021--           ###



#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np


blue = (255, 0, 0 ); green = (0, 255, 0); red = (0, 0, 255)
capturing = False
# true si el botón está presionado
mode = False
k = 0
xybutton_down = -1, -1

img = cv2.imread('hoja.png')
print('---------- RECORTE DE IMÁGENES CON OPEN CV ---------- \n\n')
print('Seleccione sobre la imágen el recorte a guardar:')

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
        print('Recorte capturado, presione (g) si desea guardar y salir, (r) si desea volver a elegir recorte o (q) para salir: ')
        crop_img = img[y_1:y_2, x_1:x_2] #dimensiono mi recorte dentro de la imagen original
        cv2.imshow("cropped", crop_img)
        imagen = crop_img
      
        if mode == 'r':
            print('Seleccione nuevamente la sección que desea \n')    
        capturing = False
        
cv2.namedWindow('image')
cv2.setMouseCallback ('image', dibuja)
    

    
while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == (ord('g') or ord('G')): # guarda el recorte seleccionado y sale del programa
        cv2.imwrite ('resultado.png', imagen)
        print('Seleccion guardada exitosamente con el nombre: resultado.png \n')
        cv2.waitKey(1)
        break
        
    elif k == (ord('r') or ord('R')): # vuelve a elegir el rectángulo de recorte
        img [ : ] = cv2.imread('hoja.png')
        mode == 'r'
        print('Seleccione nuevamente la sección que desea:  \n')

    elif k ==  (ord ('q') or ord('Q') or 27): # con q, Q o tecla "escape" sale del programa.
        break
cv2.destroyAllWindows()
