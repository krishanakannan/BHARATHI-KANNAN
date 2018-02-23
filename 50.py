def pot(k):

    if(k == 0):

        return False

    while (k!=1):

            if((k%2)!=0):

                return False

            k=k//2

    return True

m=input()

if(pot(m)):

    print("yes")

else:

    print("no")
