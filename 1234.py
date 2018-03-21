
k=int(input())
l=list(1 for i in range(k))
n=[]
for i in range(2,k,1):
    if l[i]==1:
        for j in range(i*i,k,i):
            l[j]=0
        if k%i==0:
            n.append(i)
print(" ".join(str(x) for x in n))
