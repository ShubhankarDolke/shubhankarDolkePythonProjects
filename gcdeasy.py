# Q.write a python program to compute the gcd of two numbers.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print(f"The GCD of {num1}, {num2} is {gcd}")





