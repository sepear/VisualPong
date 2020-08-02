import pygame,cv2

import numpy as np


def prueba():
    
    
    return( (255,255,255) )

#azul el primero

#color= [[114,128,142,255,73,255],[48,78,56,188,64,255]]
color= [114,128,142,255,73,255]

def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",imgHSV)
    lower = np.array(color[0:3])
    upper = np.array(color[3:6])
    mask = cv2.inRange(img,lower,upper)
    x,y=getContours(mask)
        #cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
      
    cv2.imshow(str(color[0]),mask)
    return x,y
    
    
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>50:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y+h//2#esto lo he tocado
 
#def drawOnCanvas(myPoints,myColorValues):
#    for point in myPoints:
#        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

'''
def funcion():
    while True:
        success, img = cap.read()
        imgResult = img.copy()
        newPoints = findColor(img, myColors,myColorValues)
        if len(newPoints)!=0:
            for newP in newPoints:
                myPoints.append(newP)
        if len(myPoints)!=0:
            drawOnCanvas(myPoints,myColorValues)
     
     
        cv2.imshow("Result", imgResult)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break 
        '''