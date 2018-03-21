a=input("Enter any line:")
st=list(a)
for x in range(len(st)-1):
	if st[x]==' ' and st[x+1]==" ":
		st[x]=''
c=''
for x in st:
	c=c+x
print(c.strip())
