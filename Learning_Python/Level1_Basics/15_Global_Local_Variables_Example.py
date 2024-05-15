# Local variable has the highest priority

a = 10
b = 20

print ("initial",a)
print ("initial",b)

def Test_Function():
    a= 50
    global b
    b= 60
    print ("inside",a)
    print ("inside",b)

Test_Function()

print ("later",a)
print ("later",b)
