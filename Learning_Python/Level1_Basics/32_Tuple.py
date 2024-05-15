#tuple --> Immutable ( chaning an element is not possible )
#list --> Mutable
numbers = (1,2,3,4,5,6,7)
print(numbers)
print(numbers[4])

tup1 = ('aakash','divya','atharva')
tup2 = ("35","32","4")
print(tup1+tup2)
print(len(tup1))

tup_a =(32,7,5,6,33,87,1)
tup_a_sorted = sorted(tup_a)
print(tup_a)
print(tup_a_sorted)
print(tup_a.index(33))