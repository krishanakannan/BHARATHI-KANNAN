k=input("Enter your string:")
a=0
for x in k:
	if x.isnumeric():
		a=a+1
if(a==len(k)):
	print("Yes")
else:
	print("No")
