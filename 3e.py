k=input("Enter any line:")
li=k.split(" ")
a=[]
for x in li:
	count=[0]*256
	maxi=-1
	for y in x:
		count[ord(y)]+=1
		if maxi<count[ord(y)]:
			maxi=count[ord(y)]
			ans=y
	a.append(ans)
for x in a:
	print(x,"",end=" ")
