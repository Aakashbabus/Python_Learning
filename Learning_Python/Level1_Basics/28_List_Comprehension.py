# Example 1
x = []

for i in range(11):
    z = i ** 2
    x.append(z)

print(x)

# Syntax:
# [expression for item in list {if(test expression)}]
y = [i ** 2 for i in range(11)]
print(y)

# Example 2

x = []

for i in range(11):
    if i % 2 == 0:
        z = i ** 2
        x.append(z)

y = [I ** 2 for I in range(11) if I ** 2 % 2 == 0]
print(y)
