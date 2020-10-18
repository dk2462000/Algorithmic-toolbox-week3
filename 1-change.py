# Uses python3



def get_change(m):

    c=m//10
    m=m%10
    
    b=m//5
    m=m%5
    

    a=m

    return a+b+c

m = int(input())
print(get_change(m))