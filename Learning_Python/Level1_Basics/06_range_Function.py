#range
#start value:
#end value#step

# by default the end value is considered as the input , step is assumed to be 1 and start as 0
n=list(range(7))
print(n)

# by default the end value is considered as the input , step is assumed to be 1
n=list(range(2,11))
print(n)

# if all 3 arguments are passed then no assumption is made
n= list(range(2,11,2))
print(n)