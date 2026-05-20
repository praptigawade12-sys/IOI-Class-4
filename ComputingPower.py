def compute_power(x,y):
    res = 1
    while (y > 0):
        if (y % 2 == 0):
            x = x*x
            y >>= 1
        else:
            res = res * x
            y -= 1

    return res

x = int(input("Enter for x in x^y: "))
y = int(input("Enter for y in x^y: "))

print("Total: ",compute_power(x,y))