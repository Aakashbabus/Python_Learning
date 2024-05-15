A = 'aakasH'
A.capitalize()
print(A)  # Aakash is the output
print(A.upper())  # AAKASH is the output
print(A.lower())  # aakash is the output

a = '7'
print(a.isnumeric())
print(a.isalpha())


#a = 7
#print(a.isnumeric())

a = 'Mike Is a good boy'
#    012345678
print(a.startswith('Mike'))  # returns true
print(a.startswith('Aakash'))  # returns false
print(a.endswith('boy'))  # returns true

a.replace('Mike', 'Aakash')
print(a)

print(a.find('a'))

# Stripoff Function

a = '   Mike Is a good boy  '
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.split())
print(a.splitlines())
print (a)

b= 'Mike' , 'Nick'
print(b)
c= ','
print(c.join(b))
