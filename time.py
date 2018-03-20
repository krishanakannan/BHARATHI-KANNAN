try :
	m=raw_input("time (hh:mm) : ")
	n=raw_input("time (hh:mm) : ")
	ans=0
	a=m.split(':')
	b=n.split(':')
	c=int(a[0])*60+int(a[1])
	d=int(b[0])*60+int(b[1])
	if(c>d):
		k=c-d
	else:
		k=d-c
	print k
except :
	print "Invalid"
