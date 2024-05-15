# Example 1  - How + operator overloading by default works in Python ( as adder and as concatenate)
# in this case a and b are numbers so + operator is performing addition
a = 2
b = 3
print(a + b)

# in this case x and y are strings so + operator is performing concatenation
x = '2'
y = '3'
print(x + y)


# Example 2 : lets see how we could overload + operator in classed of
class Store:

    def __init__(self, mangoes, bananas):
        self.mangoes = mangoes
        self.bananas = bananas

    # Here we are overloading the addition Operator to perform store attributes addition
    def __add__(self, other):
        mangoes = self.mangoes + other.mangoes
        bananas = self.bananas + other.bananas
        return Store(mangoes, bananas)


Store1 = Store(4, 1)
Store2 = Store(6, 7)

total = Store1 + Store2

print(total.mangoes)
print(total.bananas)
