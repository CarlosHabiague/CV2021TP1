###     TP9_Homografía_Rectificación con Eventos del mouse    ###
###                                                           ###
### NOTA: Se carga una imágen y luego:                        ###
###      - Manteniendo y soltando el clik izquierdo del       ###
###       mouse se imprime la medida en cm.                   ###
###   (r o R) Recarga al imágen limpia sin las medidas.       ###
###   (q o Q o ESCAPE) Salir.                                 ###
###                                                           ###
### Alumno: HABIAGUE, Carlos.                                 ###
###                                                           ###
###             --"VISIÓN POR COMPUTADORA" 2021--             ###


import cv2
import numpy as np
import math

blue = (255, 0, 0); green = (0, 255, 0); red = (0, 0, 255); yellow = (0, 255, 255);    #Define colores

drawing = False
ix, iy = 0, 0

print('---------- TRANSFORMACIONES DE IMÁGENES CON OPEN CV ---------- \n\n')
print('--- A partir de una imágen, se realiza la rectificación automática. ---')
print('--- Con datos medidos reales se puede conocer cualquier distancia dentro del plano rectificado de la imágen. ---\n')
print('/// Las medidas reales de la puerta son:')
print('*Ancho de la puerta: 102 cm \n')
print('*Alto de la puerta: 210 cm. ///')

def homografia(image, origen, destino):                 #Recibe los 4 pares de puntos.
    (al, an) = image.shape[:2]

    M = cv2.getPerspectiveTransform(origen, destino)    #Matriz homografia

    img_out = cv2.warpPerspective(image, M, (an,al))    #Transformacion homográfica:
    return img_out

def medicion(event, x, y, flags, param):                #Medición e impresión de mediciones sobre la pantalla

    global ix, iy, drawing, img_rect, img_rec_copia, img_rect_medida
    
    if event == cv2 .EVENT_LBUTTONDOWN:                 #Pulsando botón izq empiezo a medir
        ix, iy = x, y
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:                  #Grafica a medida que se mueve el mouse
        if drawing is True:
            img_rect[:] = img_rect_medida[:]                                    
            cv2.line(img_rect, (ix, iy), (x, y), red, 2)
            medida = (np.sqrt((ix-x)**2+(iy-y)**2))            #Cálculo de longitud en cm (Distancia entre dos puntos)
                                                                           
            x_y_text = int((ix+x)/2+10), int((iy+y)/2-10)      #Coordenadas del texto                                
            cv2.putText(img_rect, "{:.2f} cm" .format(medida), (x_y_text), cv2.FONT_HERSHEY_PLAIN, 1, yellow, 1) #Imprime texto

    elif event == cv2.EVENT_LBUTTONUP:                  #Termina de graficar soltando botón izquierdo
        img_rect_medida[:] = img_rect[:]
        drawing = False

image = cv2.imread('frente_en_colombia.jpg')                       #Imagen a rectificar
(h,w) = (210, 102)                                                 #Tamaño de la puerta en cm
                                                        #DATOS OBTENIDOS CON PHOTOSHOP:
x1=916; y1=424;                                         #Vértice superior izquierdo de la puerta
x2=1808; y2=548;                                        #Vértice superior derecho de la puerta
x3=932; y3=2440;                                        #Vértice inferior izquierdo de la puerta
x4=1800; y4=2276;                                       #Vértice inferior derecho de la puerta

destino = np.float32([[x1,y1],[x1+w,y1],[x1,y1+h],[x1+w,y1+h]])    #4 vertices con offset para ver toda la imagen
origen = np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])             #Puntos seleccionados 
        
img_rect = homografia(image,origen,destino)             #Transformación homográfica de la imagen y dos copias
img_rect_copia = img_rect.copy()
img_rect_medida = img_rect.copy()
cv2.imwrite('Imagen_rectificada.jpg',img_rect)          #Guardo la imagen rectificada
        
cv2.namedWindow('Rectificada')
cv2.setMouseCallback('Rectificada',medicion) #Cuando hay un evento del mouse llama a esta función

while True:
    cv2.imshow('Rectificada', img_rect)               #Muestro imagen rectificada 
    
    k = cv2.waitKey(1) & 0xFF

    if k == (ord('q') or ord('Q') or 27):              #Sale al presionar 'q' o 'Q' o ESC
        break

    if k == (ord('r') or ord('R')):                    #Con 'r' o 'R' restauramos la medición
        img_rect = img_rect_copia.copy()                        
        img_rect_medida = img_rect.copy()
        
cv2.imwrite('Imagen_con_mediciones.jpg',img_rect)       #Guardo la imagen rectificada

cv2.destroyAllWindows()                                 #Cierra las ventanas

