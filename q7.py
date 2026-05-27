class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    
# __init__ method naming the attributes make, model, and year
    def __init__(self, make, model, year):  
        self.make = make
        self.model = model
        self.year = year

# describe_car method to print the car's information in the format "Year Make Model"
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")
   

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

# Create an instance of the Car class with the specified attributes make, model, and year. Car(...) calls the __init__ method to initialize the attributes of the Car instance.
my_car = Car("Toyota", "Corolla", 2020)

# the .describe_car method tells Python to execute the method defined inside the class for that specific object.
my_car.describe_car()
