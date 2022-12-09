# write a Python program to evaluate the Fibonacci series for n terms
def fibonacci(x):
    if x <= 0:
        return "Incorrect Input"
    farray = [0, 1]
    if x > 2:
        for i in range(2, x):
            farray.append(farray[i - 1] + farray[i - 2])
            # print(farray)
    return farray[x - 1]


n = int(input("Enter the place : "))
# a = n + 1
print(fibonacci(n))
