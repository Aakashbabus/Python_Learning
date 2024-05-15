#a=2
#b=0
#print (a/b)

# i dont want to abort here , i dont want a trackeback

try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError:
    print('There is a zero division error')
finally:
    print('Continue with the following code ')

try:
    a=2
    b=1
    print(a/b)
except ZeroDivisionError:
    print('There is a zero division error')
finally:
    print('Continue with the following code ')