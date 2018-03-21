def gcd(k,b):
    while b > 0:
        k, b = b, k % b
    return k
def lcm(k, b):
    return k * b / gcd(k, b)
k,b=map(int,input("Enter the values:").split(' '))
print(int(lcm(k,b)))
