k=int(input())
v=0
while(k>0):
    dig=k%10
    v=v*10+dig
    k=k//10
print(v)
