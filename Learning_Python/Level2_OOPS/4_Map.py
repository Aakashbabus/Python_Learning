
print(list(filter(lambda a:a%2==0,range(10))))
print(list(filter(lambda a:a**2,range(10))))

# while the filter will only return true of false , map can rerturn andwers
print(list(map(lambda a:a**2,range(10))))
print(list(map(lambda a:a%2==0,range(10))))
