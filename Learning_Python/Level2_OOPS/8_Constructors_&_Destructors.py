'''
In Python, constructors and destructors are special methods used in classes for initialization and cleanup tasks,
respectively. Here's how they're used:

Constructors:
Constructors are special methods named __init__(). They are automatically called when a new instance of a class is
created.The primary purpose of a constructor is to initialize the attributes of the newly created object.
Constructors can take arguments to initialize the object with specific values.

Destructors:
Destructors are special methods named __del__(). They are called when an object is about to be destroyed.
The primary purpose of a destructor is to perform cleanup tasks before the object is removed from memory.
However, it's important to note that in Python, destructors are not commonly used because Python has a
garbage collector that automatically manages memory, reclaiming memory occupied by unreachable objects.
'''
class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        print ("Constructed")

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

    def __del__(self):
        print("Destructed")


# Creating objects (instances) of the Car class
car1 = Car("Red", "Toyota", "Corolla", 2020)
car2 = Car("Blue", "Honda", "Civic", 2019)

# Accessing attributes
print(car1.color)  # Output: Red

# Calling methods
car1.start_engine()  # Output: Engine started.
car1.drive()         # Output: Driving...
car2.drive()         # Output: Cannot drive, engine is not running.