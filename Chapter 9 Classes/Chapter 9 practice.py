# Object-oriented programming (OOP) is one of the most effective approaches to 
# writing software. Making an object from a class is called instantiation
# dog.py By convention, capitalized names refer to classes in Python
class Dog:
    '''A simple attempt to model a dog'''

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        '''simulate a dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        print(f"{self.name} rolled over.")
my_dog = Dog('Wangcai',6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# Accessing Attributes
my_dog.name
my_dog.age
# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Working with Classes and Instances
# The Car Class
class Car:
    '''simple attempt to represent a car'''
    def __init__(self,make,model,year):
        '''initilize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an Attribute
class Car:
    '''simple attempt to represent a car'''
    def __init__(self,make,model,year):
        '''initilize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # this is the attribute set to 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        ''' Print a stmt showing the mileage of the car'''
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
    
# Modifying Attribute Values
# normally we cannot get 0 mile cars even from dealership. how to modify attribute values?
#    - change the value directly through an instance
my_new_car.odometer_reading = 23 #dot notation to access the attribute, and set its value directly
my_new_car.read_odometer()
my_new_car_1 = Car('subaru','forester',2025)
my_new_car_1.read_odometer() # above change applies to the instance only, no affect on Car method
#    - set the value through a method
class Car:
    '''simple attempt to represent a car'''
    def __init__(self,make,model,year):
        '''initilize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # this is the attribute set to 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        ''' Print a stmt showing the mileage of the car'''
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        '''Set the odmeter reading to the given value'''
        self.odometer_reading = mileage
my_new_car = Car('audi','a4',2024)
my_new_car.read_odometer()
my_new_car.update_odometer(25)
my_new_car.read_odometer()
# to make it more useful, like prevent roll back odometer, see below: 
class Car:
    '''simple attempt to represent a car'''
    def __init__(self,make,model,year):
        '''initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # this is the attribute set to 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        ''' Print a stmt showing the mileage of the car'''
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        '''
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You cannot roll back an odometer!")
my_new_car.read_odometer()
my_new_car.update_odometer(30) # succeed
my_new_car.update_odometer(-5) # fail since it is smaller than 30
#    - increment the value (add a certain amount to it) through a method
class Car:
    '''simple attempt to represent a car'''
    def __init__(self,make,model,year):
        '''initilize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # this is the attribute set to 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        ''' Print a stmt showing the mileage of the car'''
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        '''
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You cannot roll back an odometer!")
    
    def increment_odometer(self,miles):
        '''add the given amount to the odometer reading'''
        self.odometer_reading += miles
my_used_car = Car('Honda','civic',1999)
my_used_car.increment_odometer(10_000)
my_used_car.read_odometer()

# Inheritance 继承 遗传
# When one class inherits from another, it takes on the attributes and methods 
# of the first class. The original class is called the parent class, and the 
# new class is the child class
class Car:
    '''simple attempt to represent a car'''
    def __init__(self,make,model,year):
        '''initilize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # this is the attribute set to 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        ''' Print a stmt showing the mileage of the car'''
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        '''
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You cannot roll back an odometer!")
    
    def increment_odometer(self,miles):
        '''add the given amount to the odometer reading'''
        self.odometer_reading += miles
# above is the parent class Car, we will add (Car) for the child class 
class ElectricCar(Car):
    '''represent aspects of a car, specific to electric car'''

    def __init__(self,make,model,year):
        '''initialize attributes of the parent class'''
        super().__init__(make,model,year)       
        # dont forget the super() stmt, can call methods from parent class
        self.battery_size = 40  # own attributes not from parent
    
    def describe_battery(self):
        ''' print a stmt describing the battry size'''
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

# Overriding Methods from the Parent Class: simply define a method in
# the child class with the same name as the method you want to override 
# in the parent class like defining read_odometer() in child class

# Instances as Attributes. build often used classes and put it in other classes
# class Battery ...
# class Elec(Car):
#...
#   self.battery = Battery()
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):    
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """check battery size and set to 65 if not"""
        self.battery_size = 65


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class
        Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year) # attentin, no self here
        self.battery = Battery() # use defined class in a class for efficiency and reduce code redundancy

# Importing Classes
# as we see in try it yourself 9-9, files can get long, evenwhen you use inheritance and composition properly. we save'em seperately and import
from car import Car # we saved the car.py, class Car is in there
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Storing Multiple Classes in a Module: we can add class Battery and ElectricCar in the car.py too like what we did
# my_electric_car.py
from car import ElectricCar as ec # aliais
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# Importing Multiple Classes from a Module
from car import Car, ElectricCar
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Importing an Entire Module
import car
my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Importing All Classes from a Module: from module_name import * but not recommended

