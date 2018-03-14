a=int(input("Enter any number"))
flag=0
for x in range(1,a+1):
	if(a%x==0):
		flag=flag+1
if(flag>2):
	print("yes")
else:
    print("No")
