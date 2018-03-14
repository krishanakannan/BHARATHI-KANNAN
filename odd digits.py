a=int(input("Enter number:"))
b=''
while(a!=0):
	t=a%10
	if t%2!=0:
		b=b+' '+str(t)
	a=a//10
print("ODD number is",b[::-1])
