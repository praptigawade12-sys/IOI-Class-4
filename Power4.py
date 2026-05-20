def powerof4(n):
    c = 0
    if (n & (~(n & (n-1)))):
        while (n>1):
            n >>= 1
            c+=1

        if (c%2 == 0):
            return True
        else:
            return False
        
n = int(input("Enter a number: "))
if (powerof4(n)):
    print(n,"is a power of 4")
else:
    print(n,"is not a power of 4")