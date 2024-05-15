#Example 1
name = 'Aakash'
number = len(name)*3
print("Hello {} , your lucky number is {}".format(name,number))

#Example 2
example ="format() method"
string = "This is an example of {} on a string".format(example)
print(string)

#Example3

first = "apple"
second ="mango"
third = "banana"
string ="{} , {} , {}".format(first,second,third)
print (string)
string ="{2} , {1} , {0}".format(first,second,third)
print (string)

#Example4

price = 150
with_tax = price * 1.18
print(price,with_tax)
print("your invoice value is {:.2f}, including GST it is {:.2f}".format(price,with_tax))

