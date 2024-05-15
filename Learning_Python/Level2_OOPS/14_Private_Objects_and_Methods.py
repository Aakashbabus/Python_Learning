'''
While you can technically access private members in Python, it's considered a best practice to treat them as
non-public and refrain from accessing them directly from outside the class. The underscore prefix is more of a
convention to indicate to other developers that these members are intended for internal use within the class
and shouldn't be relied upon by external code.

Python prioritizes simplicity and flexibility, trusting developers to use language features responsibly rather than
enforcing strict access control rules. This approach aligns with Python's philosophy of readability and practicality,
allowing developers to focus on solving problems effectively while maintaining code clarity and simplicity.

In Python, methods and attributes prefixed with a single underscore (_) and double underscore (__) have different
meanings, particularly in terms of visibility and name mangling.

Single Underscore Prefix (_):
Naming convention: Single underscore prefix is a convention used to indicate that a method or attribute is intended for
internal use or is a non-public part of the API.
Visibility: It doesn't have any impact on the visibility of the method or attribute. It's still accessible from outside
the class.
Example: _internal_method()

Double Underscore Prefix (__):
Name Mangling: When a method or attribute name is prefixed with double underscores within a class definition, Python
performs name mangling. This means the interpreter changes the name of the method or attribute to include the class
name, effectively making it harder to accidentally override the method or access the attribute from outside the class.
Visibility: Despite name mangling, the method or attribute can still be accessed from outside the class, albeit with a
modified name.
Example: __mangled_method()

'''
class simple:

    def __init__(self):
        self.value1 = 1
        self.__value2 = 2

    def A1 (self):
        print ("Message from A1")

    def __A2 (self):
        print ("Message from A2")

exmp = simple()

print (exmp.value1)
exmp.A1()

# when you run the below commands you get a traceback because __value2 and __A1() are private as they start with __
#print (exmp.__value2)
#exmp.__A2()

# this gives the list of methods in simple
print(dir(simple))
# in the dir you can see _simple__A2 is available for use
exmp._simple__A2()

