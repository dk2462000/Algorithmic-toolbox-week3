# Uses python3

def get_optimal_value(capacity, weights, values):
    value=0
    
    fra=[]
    n=len(values)
    for i in range(n):
        fra.append(values[i]/weights[i])
        
    if capacity==0:
        return 0
    while capacity>0:
            
            m=max(fra)
            n=min(capacity,weights[fra.index(m)])
            capacity-=n 
            value+=(n/weights[fra.index(m)])*values[fra.index(m)]
            weights[fra.index(m)]-=n
            fra.remove(m)
    return value


data = list(map(int, input().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))