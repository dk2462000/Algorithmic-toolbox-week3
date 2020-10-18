n=int(input())
if n==1:
    print(1)
    print (1)
remaining=n
gift=[]
for i in range(1,n):
    if (remaining>2*i):
        gift.append(i)
        remaining-=i
    else:
        gift.append(remaining)
        break
print(len(gift))

print(" ".join([str(i) for i in gift]))
        