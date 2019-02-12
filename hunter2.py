k = []
a=int(input())

for i in range (0,a):
    e=int(input())
    k.append(str(e))
k.sort()
k.reverse()
d=" ".join(k)
print(d)
