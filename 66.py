k = input()
if k > 1:
   for i in range(2,k):
       if (k % i) == 0:
           print("No")
           break
   else:
       print("Yes")
else:
   print("No")
