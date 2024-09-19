# Function: A standalone block of code that performs a task independently
def wash_car(car):  # This function takes a car object as a parameter
    return f"Washing the {car.color} car."

# Class: A blueprint for creating objects
class Car:
    # Method: A function defined inside a class (Here: __init__)
    def __init__(self, color, model):  # Parameters: color and model
        # Attributes: Variables that belong to the object
        self.color = color  # Attribute to store the car's color
        self.model = model  # Attribute to store the car's model

    # Method: A function that belongs to the class Car
    def start_engine(self):
        # This method performs an action related to the Car object
        return "The engine is now running!"

    # Method: Another action the car can perform
    def paint(self, new_color):  # Parameter: new_color
        self.color = new_color  # Changes the car's color attribute
        return f"The car is now {new_color}."

# Object: An instance of the class Car
my_car = Car("Red", "Sedan")  # Creates a Car object with color "Red" and model "Sedan"

# Using the object's attributes
print(f"My car's color: {my_car.color}")  # Accessing an attribute
print(f"My car's model: {my_car.model}")  # Accessing another attribute

# Calling a method on the object
print(my_car.start_engine())  # Calls the start_engine method

# Calling another method on the object and changing its attribute
print(my_car.paint("Blue"))  # Calls the paint method to change the car's color

# Using a standalone function with the car object
print(wash_car(my_car))  # Calls the wash_car function with my_car as an argument

"""
Explanation of the Code:
1. Function (wash_car): This is a standalone function that takes a car object as a parameter and performs an action (washing the car).
2. Class (Car): Defines a blueprint for creating car objects. It has attributes (color and model) and methods (start_engine and paint).
3. Attributes (self.color, self.model): These belong to the car objects and store data about each car.
4. Methods (start_engine, paint): These are functions defined inside the Car class and describe the actions that a car object can perform.
5. Object (my_car): An instance of the Car class, created with specific attribute values ("Red" and "Sedan").
6. Parameters (color, model, new_color): Inputs used by the Car class's methods and the standalone function.
"""