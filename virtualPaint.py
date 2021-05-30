import cv2
import numpy as np
web=cv2.VideoCapture(0)
width=440
height=280
pooint = []#[x,y,colorID]
web.set(3,width)
web.set(4,height)
web.set(10,150)
colorSet=[[0,141,199,48,237,255],
[23,132,234,81,255,255],
[88,188,239,121,255,255]]
colorValue=[[61,64,242],
            [61,242,124],
            [242,170,61]]
def getColors(img):
    count=0
    imghsv=cv2.cvtColor(imgweb,cv2.COLOR_BGR2HSV)
    global colorSet
    global colorValue
    newPoint=list()
    for color in colorSet:
        Min = np.array(color[0:3])
        Max = np.array(color[3:6])
        mask=cv2.inRange(imghsv,Min,Max)
        x,y= getContours(mask)
        cv2.circle(imageResult,(x,y),10,colorValue[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoint.append([x,y,count])
        count+=1
    return newPoint

def getContours(img):
    countour, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in countour:
        area= cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y

def draw(Mypoints,clrval):
    for point in Mypoints:
        cv2.circle(imageResult,(point[0],point[1]),5,clrval[point[2]],cv2.FILLED)
Mypoint=list()
while True:
    success, imgweb = web.read()
    imageResult=imgweb.copy()
    newPoint = getColors(imgweb)
    if len(newPoint)!=0:
        for p in newPoint:
            Mypoint.append(p)
    if len(Mypoint)!=0:
        draw(Mypoint,colorValue)
    cv2.imshow("test",imageResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
