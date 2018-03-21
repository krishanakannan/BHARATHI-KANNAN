
k=int(input(""))
m=[]
for a in range(0,k):
	b=int(input(""))
	m.append(b)
for a in range(0,k-1,1):
	for b in range(a+1,k,1):
		if m[a]<m[b]:
			c=m[a]
			m[a]=m[b]
			m[b]=c
for a in range(0,k,m):
	if a>0 and a<k-1:
		if m[a]!=m[a+1] and m[a]!=m[a-1]:
			print(m[a])
	elif a==0:
		if m[a]!=m[a+1]:
				print(l[a])
	elif a==k-1:
		if m[a]!=m[a-1]:
				print(m[a])
