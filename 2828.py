a=input("Enter the string:")
b=list(a)
for x in range(len(b)):
	if b[x]==' ':
		b[x]=''
c=''
for x in b:
	c=c+x
print(c.strip())
