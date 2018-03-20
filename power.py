a=int(input(""))
x=a
k=0
while(x>0):
	r=x%10
	x=x//10
	k=k+(r**2)
print(k)
