a = int(input())
n1 = 0
n2 = 1
count = 0
if a <= 0:
   print("Please enter a positive integer")
elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(n1)
else:
   print("Fibonacci sequence upto",a,":")
   while count < a:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
