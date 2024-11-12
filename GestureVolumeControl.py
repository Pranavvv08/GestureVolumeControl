import cv2
import time
import numpy as np
import handTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam,hCam=640,480

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volumeRange = volume.GetVolumeRange()

minVolume=volumeRange[0]
maxVolume=volumeRange[1]
volBar=300
vol=0

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
prevTime=0

detector=htm.HandDetector(detectionConfidence=0.8)


while True:
    success,img=cap.read()
    img=detector.findHands(img,draw=False)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        x1,y1=lmList[4][1],lmList[4][2]
        x2,y2=lmList[8][1],lmList[8][2]
        
        cx,cy=(x1+x2)//2,(y1+y2)//2
        
        cv2.circle(img,(x1,y1),10,(0,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(0,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)
        cv2.circle(img,(cx,cy),10,(0,0,255),cv2.FILLED)
        
        length=math.hypot(x2-x1,y2-y1)
        
        if length<40:
            cv2.circle(img,(cx,cy),10,(0,255,255),cv2.FILLED)
        if length>290:
            cv2.circle(img,(x1,y1),13,(0,255,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),13,(0,255,255),cv2.FILLED)
            
        vol=np.interp(length,[40,290],[minVolume,maxVolume])
        volBar=np.interp(length,[40,290],[300,150])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)

    cv2.rectangle(img,(10,150),(20,300),(193,223,255),2)
    cv2.rectangle(img,(10,int(volBar)),(20,300),(193,223,255),cv2.FILLED)
        
    currentTime=time.time()
    
    fps=1/(currentTime-prevTime)
    prevTime=currentTime
    
    cv2.putText(img,f'FPS:{int(fps)}',(5,15),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
    
    cv2.imshow("Image",img)
    if cv2.waitKey(33) & 0xFF == ord('e'):
        break
cap.release()
cv2.destroyAllWindows()
    