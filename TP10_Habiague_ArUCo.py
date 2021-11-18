###                        TP10_ArUCo                         ###
###                                                           ###
### NOTA: no tuve tiempo para la parte del video profe..      ###
###         pero lo voy a intentar hacer antes del viernes    ###
###         imprí los 4 ArUCos para poder marcar las esquinas ###
###         del video...                                      ###
###                                                           ###
###                                                           ###
### Alumno: HABIAGUE, Carlos.                                 ###
###                                                           ###
###             --"VISIÓN POR COMPUTADORA" 2021--             ###


import cv2
import cv2.aruco as aruco
import numpy as np

def findMarkers(img, markerSize=6, totalMarkers=250, draw = True): # marcadores de 6x6 
	gray = cv2.cvtColor (img,cv2.COLOR_BGR2GRAY)
	key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')      
	arucoDict = aruco.Dictionary_get(key)
	arucoParam = aruco.DetectorParameters_create()
	bb ,ids,rejected = aruco.detectMarkers(img, arucoDict, parameters= arucoParam)
	if draw:
		aruco.drawDetectedMarkers (img, bb)
	return [bb, ids]

def replacementAruco(bb,id, img, img_r , drawId = True):
	ul=bb[0][0][0], bb[0][0][1]
	ur=bb[0][1][0], bb[0][1][1]
	dr=bb[0][2][0], bb[0][2][1]
	dl=bb[0][3][0], bb[0][3][1]

	h,w = img_r.shape[:2]

	pt1 = np.array([ul,ur,dr,dl])
	pt2 = np.float32 ([[0,0],[w,0],[w,h],[0,h]])
	mtx, _= cv2.findHomography (pt2,pt1)
	img_out = cv2.warpPerspective (img_r, mtx, (img.shape[1], img.shape[0]))

	cv2.fillConvexPoly (img, pt1.astype(int),(0,0,0))
	img_out = img + img_out

	return img_out

mask1 = cv2.imread('imag1.jpg')
mask2 = cv2.imread('imag2.jpeg')



cap = cv2.VideoCapture(0)

ret, frame = cap.read()                                 
H = len(frame)                                        
W = len(frame[0])                                      
framesize = (W, H) 
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
fps = cap.get(cv2.CAP_PROP_FPS)                         
out = cv2.VideoWriter('salida.avi', fourcc, fps, framesize)

while (True):

	ret, img = cap.read()
	arucoFound= findMarkers(img)

	
	if len(arucoFound[0])!=0 and arucoFound[1]==1:  #implanta imágen 1
		for bb, id in zip (arucoFound[0],arucoFound[1]):		
			img = replacementAruco (bb,id,img,mask1)

	
	if len(arucoFound[0])!=0 and arucoFound[1]==2:    # implanta imágen 2
		for bb, id in zip (arucoFound[0],arucoFound[1]):		 
			img = replacementAruco (bb,id,img,mask2)
	
	cv2.imshow ("Aruco", img)
	k = cv2.waitKey(1) & 0xFF
	out.write(img)

	#Sale al presionar 'q'
	if k == ord('q'):                                            
		cv2.destroyAllWindows()
		break
