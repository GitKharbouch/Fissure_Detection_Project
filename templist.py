l1,lj=[],[]
j=0

def temp(x,y,w,h):
        global j,lj,l1      
        lj.append(x),lj.append(y),lj.append(w),lj.append(h)     #Get coordinates
        l1.insert(j,lj)                                         #Insert coordinate list and frame number j
        j=j+1
        lj=[]
        
        
        
    