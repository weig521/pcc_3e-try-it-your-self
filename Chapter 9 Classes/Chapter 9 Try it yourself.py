'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating 
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually,
and then call both methods.'''
class Restaurant:
    '''create restaurant class with name and cuisine type'''
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and the cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"The restaurant is open now.")
restaurant = Restaurant("Chili's",'Dinner')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.'''
golden_corral = Restaurant('Golden Corral','Buffet')
golden_corral.describe_restaurant()
papa_johns = Restaurant('Papa Johns','Pizza')
papa_johns.describe_restaurant()
red_lobster = Restaurant('Red Lobster','Dinner')
red_lobster.describe_restaurant()

'''9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods for each.'''
class User:
    '''class user with first and last names and other attributes'''
    def __init__(self,first_name,last_name,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, gender is {self.gender}.")
    def greet_user(self):
        print(f"Hi {self.first_name.title()} {self.last_name.title()}, welcome!")
will_smith = User('will','smith','male')
will_smith.describe_user()
will_smith.greet_user()
taylor_swift = User('Taylor','Swift','Female')
taylor_swift.describe_user()
taylor_swift.greet_user()

'''9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Classes   167
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.'''
class Restaurant:
    '''create restaurant class with name and cuisine type'''
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        '''Display a msg about the name and cuisine type of restaurant'''
        print(f"The name of the restaurant is {self.name} and the cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        '''Indicate that the restaurant is open'''
        print(f"The restaurant is open now.")
outback_2546 = Restaurant('outback','dinner')
outback_2546.number_served # return 0 same as our default number
outback_2546.number_served = 167
outback_2546.number_served # now it is 167

class Restaurant:
    '''create restaurant class with name and cuisine type'''
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        '''Display a msg about the name and cuisine type of restaurant'''
        print(f"The name of the restaurant is {self.name} and the cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        '''Indicate that the restaurant is open'''
        print(f"The restaurant is open now.")
    def set_number_served(self,number):
        '''to set the number of served customers'''
        self.number_served = number
outback_2546 = Restaurant('outback','dinner')
outback_2546.number_served
outback_2546.set_number_served(199)
outback_2546.number_served

class Restaurant:
    '''create restaurant class with name and cuisine type'''
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        '''Display a msg about the name and cuisine type of restaurant'''
        print(f"The name of the restaurant is {self.name} and the cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        '''Indicate that the restaurant is open'''
        print(f"The restaurant is open now.")
    def set_number_served(self,number):
        '''to set the number of served customers'''
        self.number_served = number
    def increment_number_served(self,count):
        '''display the increased count to the served customers'''
        self.number_served =+ count

outback_2546 = Restaurant('outback','dinner')
outback_2546.number_served
outback_2546.increment_number_served(88)
outback_2546.number_served

'''9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''
class User:
    '''class user with first and last names and other attributes'''
    def __init__(self,first_name,last_name,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        '''Print user info'''
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, gender is {self.gender}.")

    def greet_user(self):
        '''print welcome message with their name'''
        print(f"Hi {self.first_name.title()} {self.last_name.title()}, welcome!")
    
    def increment_login_attempts(self):
        '''increase the login attempts by 1'''
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        '''Reset the login attempts to 0'''
        self.login_attempts = 0

adam_smith = User('adam','smith','male')
adam_smith.increment_login_attempts()
adam_smith.login_attempts

i = 1
while i <= 5:
    adam_smith.increment_login_attempts()
    i += 1
adam_smith.login_attempts
adam_smith.reset_login_attempts()
adam_smith.login_attempts

'''9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.'''
class Restaurant:
    '''create restaurant class with name and cuisine type'''
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        '''Display a msg about the name and cuisine type of restaurant'''
        print(f"The name of the restaurant is {self.name} and the cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        '''Indicate that the restaurant is open'''
        print(f"The restaurant is open now.")
    def set_number_served(self,number):
        '''to set the number of served customers'''
        self.number_served = number
    def increment_number_served(self,count):
        '''display the increased count to the served customers'''
        self.number_served =+ count

class IceCreamStand(Restaurant):
    '''A ice cream stand with diff icecream flavors'''

    def __init__(self,name,cuisine_type):
        '''initialize attributes'''
        super().__init__(name,cuisine_type)
        self.flavors = ['vanilla','chocolate','strawberry']
    
    def display_flavors(self):
        ''' display all the flavors of the icy stand'''
        print(f"\nThe flavors {self.name.title()} has: ")
        for flavor in self.flavors:
            print(flavor)

little_icy = IceCreamStand('little icy','ice cream')
little_icy.display_flavors()

'''9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.'''
class User:
    '''class user with first and last names and other attributes'''
    def __init__(self,first_name,last_name,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        '''Print user info'''
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, gender is {self.gender}.")

    def greet_user(self):
        '''print welcome message with their name'''
        print(f"Hi {self.first_name.title()} {self.last_name.title()}, welcome!")
    
    def increment_login_attempts(self):
        '''increase the login attempts by 1'''
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        '''Reset the login attempts to 0'''
        self.login_attempts = 0

class Admin(User):
    '''write a child class of User with new attribute'''

    def __init__(self, first_name, last_name, gender):
        '''initialize attributes of the parent class and its own attributes'''
        super().__init__(first_name, last_name, gender)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"\nThe administrator {self.first_name.title()} {self.last_name.title()} has the following previleges: ")
        for privilege in self.privileges:
            print(privilege)

karl_marx = Admin('karl','marx','male')
karl_marx.show_privileges()

'''9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.'''
class Privileges:
    '''privileges to be an administrator'''

    def __init__(self):
        '''initialize attributes'''
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        ''' print a message showing the admi privileges'''
        print(f"The admi privileges are: ")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    '''write a child class of User with new attribute'''

    def __init__(self, first_name, last_name, gender):
        '''initialize attributes of the parent class and its own attributes'''
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()

karl_marx = Admin('karl','marx','male')
karl_marx.privileges.show_privileges()

'''9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 65 if it isn’t already. Make
an electric car with a default battery size, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase in the car’s range'''
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

my_new_ecar = ElectricCar('tesla','s',2024)
my_new_ecar.battery.get_range()
my_new_ecar.battery.upgrade_battery() # upgrade the default 40 to 65, below show range 225 from 150
my_new_ecar.battery.get_range()

'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a 
Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.'''
from restaurant import Restaurant
applebee_216 = Restaurant("apple bee's",'dinner')
applebee_216.increment_number_served()

'''9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
the classes User, Privileges, and Admin in one module. Create a separate file,
make an Admin instance, and call show_privileges() to show that everything is
working correctly.'''
from user import Admin
warren_buffett = Admin('warren','buffett','male')
warren_buffett.privileges.show_privileges()

'''9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly'''
# I did not do this one, just use two import stmt to get the necessary classes from the two modules

'''9-13. Dice: Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times.'''
from random import randint
class Die:
    ''' roll die '''
    
    def __init__(self,sides = 6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1,self.sides))
roll = Die()
for i in range(10):
    roll.roll_die()

'''9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize'''
list = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
from random import sample
winner = sample(list,4)
print(f"People who match all the four below win: ")
for i in winner:
    print(i)

'''9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
a loop that keeps pulling numbers until your ticket wins. Print a message reporting 
how many times the loop had to run to give you a winning ticket.'''
my_ticket = {'a',1,3,8}
i = 1
active = True
while active:
    winner = sample(list,4)
    i+=1
    if set(winner) == my_ticket:
        break
print(f"It takes {i} times to win.") # in my case, 4457 times draws used to win

