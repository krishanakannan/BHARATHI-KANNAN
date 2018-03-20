l=int(input())
b=int(input())
k=0
while True:
    l=l+1
    if l%2==0:
        d=0
    elif l>=b:
        break
    else:
        k+=1
print(k)
