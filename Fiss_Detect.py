import torch
import cv2 as cv
import pandas as pd
import critic
import templist
import time

X,Y,W,H,IMG,TIME=[],[],[],[],[],[]
i=0
idimg=0


model = torch.hub.load('yolov5-master', 'custom',
path='yolov5-master\models\MODEL_V2.pt', source='local',force_reload=True)    #loading the custom model


cap = cv.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
     # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame")
        break
    frame=cv.resize(frame,[640,640])    #dimensions our models was trained with
    results=model(frame)                #applying the model on he frame
    result = results.xyxy[0].tolist()   #getting coordinates
    
    if len(result)!=0:
        for pred in result:
            cv.rectangle(frame,(int(pred[0]),int(pred[1])),((int(pred[2])),(int(pred[3]))),(255,0,0),2)
            cv.imwrite('images/{}.png'.format(idimg),frame)
            if len(critic.count)>20 :
                critic.count=[]
                i=0
            X.append(pred[0])
            Y.append(pred[1])
            W.append(pred[2])
            H.append(pred[3])
            IMG.append('images/{}.png'.format(idimg))
            TIME.append(time.ctime())
            
            critic.critic(X[i],Y[i],W[i],H[i],i)
           
            
            if critic.critique == True:
               data=pd.DataFrame({'X':X,'Y':Y,'W':W,'H':H,'IMG_ID':IMG,'TIME':TIME})
               data.to_excel('Fissure_data.xlsx')  
               
            i=i+1
            idimg=idimg+1
            
           
    
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break




        