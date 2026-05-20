def Power2(num):
    if (num==0):
        return 0
    if ((num & (~(num-1))) == num):
        return 1
    return 0

n = int(input("Enter the number"))
if (Power2(n)):
    print("\n The number is power of 2")
else:
    print('\n Then number is not power of 2')