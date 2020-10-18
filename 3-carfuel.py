def computeminrefill(distance, tank, stops):
    num=0
    before=0
    i=0
    
   
        
    stops.append(distance)
    print(stops)
    
    while i<len(stops):
          
       
        if stops[i]-before<=tank :
            i+=1
            continue
        elif stops[i]-stops[i-1]>tank or i==0:
            return -1
        else:
            before=stops[i-1]
            num+=1    
    return num
  
d=int(input())
t=int(input())
n=int(input())

lst=list(map(int,input().split()))

print(computeminrefill(d,t,lst))
