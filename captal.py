
try:
    m =raw_input("enter a string")
    if(len(m)<=1000000):
        a = list(m)
        if(96<ord(a[0])<123):
            a[0] = chr(ord(a[0])-32)
        for x in range(1,len(m)-1):
            if((a[x] == ' ') and (96<ord(a[x+1])<123)):
                a[x+1] = chr(ord(a[x+1])-32)
        b= ''
        for x in a:
            b=b+x
        print(b)
    else:
        raise Exception
except:
    print("Invalid Input")
