#FACTORIAL

#0! = 1
#1! = 1 * 0! = 1 * 1 = 1
#2! = 2 * 1! = 2 * 1 = 2
#3! = 3 * 2! = 3 * 1 = 6
#4! = 4 * 3! = 4 * 6 = 24

def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial (n-1)

result = factorial(20)
print ( "Factorial is", result )
