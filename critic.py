count=[]                                            #Variable that keeps track of fissures and frame number
critique=False

def critic(x,y,w,h,conf,j):
    global count,critique
    if w>120 or h>120  :   c=True        #Limits will be set depending on conveyer material    
    else:   c=False
          
    if c==True and conf[j]>= 0.5 :                                     #critic on two successive frames->critique = true
                                                                    #and confidence >= 05
        count.append(j)
        if len(count)>3:
            if  count[j-1]!=0 and count[j-2] !=0 :
                critique=True
            else : critique=False
        else : critique=False

    else  :
        count.append(0)
        critique=False
        
    
