try:
	k=0
	n=str(raw_input())
	a=[]
	p=str()
	for i in range (0,len(n)):
		a.append(n[i])
	if len(n)%2==0:
		j=len(n)
	else:
		j=len(n)-1
	while(k!=j):
		t=a[k]
		a[k]=a[c+1]
		a[k+1]=t
		k=k+2
	for i in range (0,len(a)):
		p=p+a[i]
	print p
except:
	print "Invalid"
