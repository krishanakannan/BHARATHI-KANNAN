
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
flag=0
c=a*b
for x in range(1,max(a,b)+1):
	l=x*x
	if l==c:
		flag=1
if (flag==0):
	print("NO")
else:
	print("Yes")
