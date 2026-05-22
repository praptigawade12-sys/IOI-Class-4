def powerof8(n):
    c = 0
    if (n & (~(n & (n-1)))):
        while(n>1):
            n >>= 1
            c += 1

        if (c % 3 == 0):
            return True
        else:
            return False
    return False

n = int(input("Enter you number: "))
if (powerof8(n)):
    print(n," is a power of 8")
else:
    print(n,"is not a power of 8")