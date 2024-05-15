# FILTER
# filter (function,iterable)

# EXAMPLE 1

def even(a):
    return a%2==0

numbers= [1,2,3,4,5,6,7,8,9,10,11]

ans = filter (even,numbers)
print(ans)

# you will have to collect the data as a list or a tuple
ans = list(filter (even,numbers))
print(ans)

# EXAMPLE 2

print(list(filter(lambda a:a%2==0,range(11))))

