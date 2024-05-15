'''
In object-oriented programming (OOP), classes, objects, attributes, and methods are fundamental concepts that help
organize and structure code in a way that mirrors real-world entities and behaviors. Here's a breakdown:

Class:
A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods)
that objects of that class will have.Think of a class as a cookie cutter and objects as the cookies. The class defines
the shape and characteristics of the cookie, while objects are the actual instances created using that template.

Objects:
An object is an instance of a class. It's a concrete entity that exists in memory and has its own set of attributes and
behaviors as defined by its class.Using our previous analogy, if a class is a cookie cutter, an object is a specific
cookie made using that cutter. Each cookie can have its own unique attributes, like decoration or flavor, while still
being based on the same template.

Attributes:
Attributes are the data members of a class, also known as fields or properties. They represent the characteristics or
state of an object.For example, if we have a class representing a car, its attributes could include things like color,
make, model, and year.

Methods:
Methods are functions defined within a class that define the behaviors or actions that objects of that class can perform.
Methods can access and modify the object's attributes, and they can also interact with other objects or the system as a
whole.Continuing with the car example, methods for a car class might include 'start_engine()', 'accelerate()', 'brake()'
, and 'turn()'. These methods define what a car can do.

Here's a simple Python example to illustrate these concepts:
'''
class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print("Engine started.")

    def stop_engine(self):
        self.is_running = False
        print("Engine stopped.")

    def drive(self):
        if self.is_running:
            print("Driving...")
        else:
            print("Cannot drive, engine is not running.")


# Creating objects (instances) of the Car class
car1 = Car("Red", "Toyota", "Corolla", 2020)
car2 = Car("Blue", "Honda", "Civic", 2019)

# Accessing attributes
print(car1.color)  # Output: Red

# Calling methods
car1.start_engine()  # Output: Engine started.
car1.drive()         # Output: Driving...
car2.drive()         # Output: Cannot drive, engine is not running.


'''
In this example, Car is a class that represents cars. Objects car1 and car2 are instances of the Car class. 
They have attributes such as color, make, model, and year, and methods such as start_engine(), stop_engine(), and drive().
'''