# python is a functioanl programming language

# Normal Function example
def add(i,j):
    return i+j

res = add( 1,2)

print(res)

# You can assign function to a variable

def add(i,j):
    return i+j

a = add
res = a( 1,2)

print(res)

# you can return a function itself from another function

def add(i,j):
    return i+j

def call(i,j):
    return add(i,j)

res = call( 1,2)

print(res)

# Function can also be passed as arguments in python

def add(i,j):
    return i+j

def call(i,j):
    return add(i,j)

def pas(i,j,fn):
    return fn(i,j)

res = pas( 1,2,call)

print(res)
