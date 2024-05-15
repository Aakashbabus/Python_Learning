# type of collection
# unordered
# unique elements
# {}

Set1 = {1, 2, 3, 4, 5}
print(Set1)

Set1 = {1, 2, 3, 4, 5, 1}
print(Set1)

# set functions
Set1.add(6)
print(Set1)

Set1.remove(1)
print(Set1)

print(2 in Set1)
print(55 in Set1)

# set Operations

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 3, 5, 7}
print(Set1 & Set2)  # intersection
print(Set1.union(Set2))  # union
Set1 = {1, 2, 3, 4, 5}
Set2 = {1, 2, 3}

print(Set2.issubset(Set1))
