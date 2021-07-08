### TP2_Segmentado                  ###
###                                 ###
### Alumno: HABIAGUE, Carlos.       ###
###                                 ###
###--"VISIÓN POR COMPUTADORA" 2021--###

import cv2

img = cv2.imread('hoja.png',0)
for i , row in enumerate ( img ):
    for j , col in enumerate (row ): 
        if ( col >= 200 ):
            img[i,j] = 255
        else:
            img[i,j] = 0

cv2.imwrite ('resultado.png', img )
cv2.imshow('Prueba de imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
