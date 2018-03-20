try:
    import re
    m =raw_input()
    a=[0]*26
    match = re.match("^([a-zA-Z]+)( [a-zA-Z]+)*$",m)
    if(match):
        for i in range(len(m)):
            if(m[i]!=' '):
                if(ord(m[i])>96):
                    a[ord(m[i])-97]+=1
                else:
                    a[ord(m[i])-65]+=1
        x=a.index(max(a))
        print(chr(x+97))
    else:
        raise Exception
except:
    print("Invalid Input")
