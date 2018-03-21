l=input()
m=['a','e','i','o','u']
n=list(n)
for i in n:
    if i in m:
        n.remove(i)
n=(n[::-1])
n="".join(n)
print(n)
