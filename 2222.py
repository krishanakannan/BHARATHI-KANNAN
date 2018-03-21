
try:
    import re
    n = input()
    match = re.match("^[a-zA-Z]+$",n)
    if(match):
        for i in range(len(n)):
            if(ord(n[i])>119 and ord(n[i])<123):
                print(chr(ord(n[i])-23), end = "")
            elif(ord(n[i])>86 and ord(n[i])<91):
                print(chr(ord(n[i])-23),end = "")
            else:
                print(chr(ord(n[i])+3),end = "")
    else:
        raise Exception
except:
    print("Invalid Input")
