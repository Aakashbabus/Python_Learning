l = ['Mike', 10.1, 1980]
print(l)

l.append(10)
print(l)

l.extend([10, 21])
print(l)

l.remove(10)
print(l)

del l[0]
print(l)

del l[0 : 2]
print(l)

l.clear()
print(l)

l = ['Mike', 10.1, 1980]
print(l)


l.pop(2)
# removes 1980
print(l)

l = ['Mike', 10.1, 1980]
l.insert(2, 'pop')
print(l)

# sort in ascending order
l = [17, 4, 31, 5, 88]
l.sort()
print(l)

# revers the list
l.reverse()
print(l)

l = ['Mike', 10.1, 1980]
# find the index
print(l.index(1980))

# find the length of list
print(len(l))
