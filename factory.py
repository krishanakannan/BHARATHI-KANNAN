a=int(input("Enter any number"))
b=""
for x in range(1,a+1):
	if a%x==0:
		b=b+" "+str(x)
                print(b)
	else:
		print("error")
