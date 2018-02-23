k=int(input())
l=0
while(k>0):
    dig=k%10
    l=l+dig
    k=k//10
print(l)
