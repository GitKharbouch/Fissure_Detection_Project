
import torch
import cv2 as cv
import pandas as pd
import critic
import time

X,Y,W,H,CONF,IMG,TIME=[],[],[],[],[],[],[] #coordinates,dimensions,image id,time of detection
i=0
idimg=0

data=pd.DataFrame({'X':X,'Y':Y,'W':W,'H':H,'IMG_ID':IMG,'Confidence':CONF,'TIME':TIME})
model = torch.hub.load('yolov5-master', 'custom',
path='yolov5-master\models\MODEL_V3.pt', source='local',force_reload=True)    #loading the custom model


cap = cv.VideoCapture(r'C:\Users\youss\OneDrive\Pictures\Camera Roll\vid.mp4')
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
            

            if len(critic.count)>20 and critic.count[i-1]==0 :   # if list is long and no fissures are detected
                critic.count=[]     #empty the list 
                X,Y,W,H,CONF,IMG,TIME=[],[],[],[],[],[],[]
                i=0
            
            X.append(pred[0])
            Y.append(pred[1])
            W.append(pred[2])
            H.append(pred[3])
            CONF.append(pred[4])
            IMG.append('images/{}.jpg'.format(idimg))   #storing the img id with coordinates so it can be identified in the image file
            TIME.append(time.ctime())
            
            critic.critic(X[i],Y[i],W[i],H[i],CONF,i)   #check if critic before storing the data
            
            
            if critic.critique == True:     #if the fissure detected is considered critic
               
               cv.imwrite('data/images/{}.jpg'.format(idimg),frame)     #save the fissure image
               idimg=idimg+1  
               new_row={'X':X[i],'Y':Y[i],'W':W[i],'H':H[i],'IMG_ID':IMG[i],'Confidence':CONF[i],'TIME':TIME[i]}    #add coordinates to df
               data=data.append(new_row,ignore_index=True)
               data.to_excel('data\Fissure_data.xlsx')
               
               
            i=i+1
             
           
            
           
    
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break




        