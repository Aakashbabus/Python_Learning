# list --->[] , Index value
# list = [1,2,3,4,5]

# dictionary ---> {}  … key
# dictionary = {key:value,key:value…..}

## example 1
My_dict = {'key1': 1, 'key2': '2', 'key3': [333],'key4': (444), 'key5': 5}
print(My_dict['key3'])

## example 2
Dictionary = {1: 'a', 2: 'b', 3: 'c'}
print(Dictionary[2])

## example 3 - add or delete an element
dictionary = {'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog'}
print(dictionary)
dictionary['e'] = 'elephant'
print(dictionary)
del (dictionary['c'])
print(dictionary)
## to see if a key is present in the dictionary or not
print('b' in dictionary)
print(dictionary.keys())
print(dictionary.values())

print(dictionary.get('g'))
print(dictionary.get('g', "'g' not found"))
