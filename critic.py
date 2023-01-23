count=[]                                            #Variable that keeps track of fissures and frame number
critique=0

def critic(x,y,w,h,j):
    global count,critique
    if w>100 or h>100 or w*h>1500 :   c=True        #Limits will be set depending on conveyer material    
    else:   c=False
          
    if c==True:                                     #critic on two successive frames->critique = true
        count.append(j)
        if len(count)>3:
            if  count[j-1]!=0 and count[j-2] !=0 :
                critique=True
        else : critique=False

    elif c==False :
        count.append(0)
        critique=False
        
    
