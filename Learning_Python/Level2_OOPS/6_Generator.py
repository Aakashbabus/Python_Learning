# Example 1


def fct():

    yield 1
    yield 2
    yield 3


value = fct()

print(value.__next__())
print(value.__next__())
print(value.__next__())


# Example 2

def squares():

    n = 1
    while n <= 5:
        square = n ** 2
        yield square
        n = n + 1


values = squares()

for i in values:
    print(i)
