a=input("Enter 1st string:")
b=input("Enter 2nd string:")
k=int(input("Enter K value:"))
c1=0
c2=0
for x in a:
	if x not in b:
		c1=c1+1
for x in st2:
	if x not in a:
		c2=c2+1
if(c1==c2==k):
	print("Yes")
else:
	print("No")
