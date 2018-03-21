import math
m,r =input().split()
m=int(m)
r=int(r)
print(type(i))
count=0
for q in range(m,r):
  if int(math.sqrt(q))**2==q:
      count=count+1
print(count)
