# Write a Python program to get the factorial of a non-negative integer
num = int(input("Enter a Number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for this numbers")
elif num == 0:
    print(" The factorial of 0 is 1")
else:
    # range(start, stop, step)
    for i in range(1, num+1):
        factorial = factorial * i
    # print("The factorial of", num, "is", factorial)
    print(f"The factorial of {num} is {factorial}")