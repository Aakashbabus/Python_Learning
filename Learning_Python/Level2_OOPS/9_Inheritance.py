'''
Imagine we have a base class called Face which represents a generic face. This class has some basic attributes and
methods common to all faces. Then, we can create a subclass called Smile which inherits from the Face class.
The Smile class will have additional attributes and methods specific to smiling faces while inheriting the common
attributes and methods from the Face class.

Here's how it could look in Python:
'''

class Face:
    def __init__(self, eye_color, hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color

    def speak(self):
        print("I am a face.")


class Smile(Face):
    def __init__(self, eye_color, hair_color, dimples):
        # here when super is called , we are refering to the super class from the derived class
        # this is to call the constructor of the base class
        super().__init__(eye_color, hair_color)
        self.dimples = dimples

    def show_expression(self):
        print("I am smiling!")


# Creating a generic face
generic_face = Face("brown", "black")
print("Generic face eye color:", generic_face.eye_color)  # Output: brown
generic_face.speak()  # Output: I am a face.

# Creating a smiling face
smiling_face = Smile("blue", "blonde", True)
print("Smiling face hair color:", smiling_face.hair_color)  # Output: blonde
print("Smiling face has dimples:", smiling_face.dimples)    # Output: True
smiling_face.show_expression()  # Output: I am smiling!

'''
In this example, Face is the base class, and Smile is the subclass that inherits from Face. The Face class has 
attributes like eye_color and hair_color, as well as a method speak(). The Smile class inherits these attributes 
and methods and adds an additional attribute dimples and a method show_expression().

By using inheritance, we avoid duplicating code by defining common attributes and methods in the base class, 
and we can extend or specialize the behavior by adding new attributes and methods in the subclass, as demonstrated 
with the Smile class.

In the Python program provided, the super() function is used within the Smile class to call the constructor 
(__init__() method) of its superclass (Face).
'''