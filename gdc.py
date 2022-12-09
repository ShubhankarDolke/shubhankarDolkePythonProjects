def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


a = int(input("Enter 1st Num: "))
b = int(input("Enter 2nd Num: "))

ans = gcd(a, b)
print(ans)
