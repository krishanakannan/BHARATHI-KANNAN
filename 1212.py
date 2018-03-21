a,b=map(int,input("Enter 1st line").split(' '))
a2,b2=map(int,input("Enter 2nd line").split(' '))
a3,b3=map(int,input("Enter 3rd line").split(' '))
if (a==b2 and a2==a3) or(b==b2 and b2==b3) or (abs(a-a2)==abs(a2-a3) and abs(b-b2)==abs(b2-b3)):
  print("yes")
else:
  print("no")
