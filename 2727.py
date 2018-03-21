a=input("Enter any String:")
k=''
for x in a:
	if x.islower():
		k=k+x.upper()
	elif x.isupper():
		k=k+x.lower()
print(k)
