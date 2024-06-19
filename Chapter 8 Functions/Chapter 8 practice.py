# Functions are named blocks of code designed to do one specific job.
# greeter.py
def greet_user():
 """Display a simple greeting."""
 print("Hello!")
greet_user()

'''A function call tells Python to execute the code in the function. To call a function, you write
the name of the function, followed by any necessary information in parentheses'''
# Passing Information to a Function
def greet_user(username):
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")
greet_user('jesse')

# Arguments and Parameters
# An argument is a piece of information that’s passed from a function call to a function. In the example 
# above, username is the parameter, we put jesse in, jesse is an argument
# pets.py
def describe_pet(animal_type,pet_name):
    '''Display info about a pet'''
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
# Multiple Function Calls: u can call is as many as needed
describe_pet('hamster','harry')
describe_pet('dog','wangcai')
describe_pet('cockroach','xiaoqiang')

#Order Matters in Positional Arguments 
describe_pet('xiaoqiang','cockroach')
# Keyword Arguments could solve wrong positional argument problem
describe_pet(animal_type='cat',pet_name='duke')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
describe_pet('duke') # default type dog, here not required for type
# if both have default, one none key argument means the first parameter

# Return Values
# fommatted name
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# what if there is someone with middle name? see below. default middle name is null
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name: # Python interprets non-empty strings as True
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a Dictionary
# person.py
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

# Using a Function with a while Loop
# Now we want to start a poll about people's names and their dream vacation places and save them into a dict
active = True 
places = {}
while active:
   name = input(f"Enter your name please: ")
   place = input(f"Enter your favoriate dream vacation place: ")
   places[name] = place
   print(f"Hi {name.title()}, your favorite dream vacation place is {place.title()}.")
   repeat = input(f"If you done, enter quit, or press any key to continue. ")
   if repeat.lower() == 'quit':
      active = False
print(places)
# above is the regular way we used before, if we want to use FN, see below
def name_place(dict):
   for name,place in dict.items():
      print(f"{name.title()}'s favorite dream vacation place is {place.title()}.")
active = True
places = {}
while active:
   name = input(f"Enter your name please: ")
   place = input(f"Enter your favoriate dream vacation place: ")
   places[name] = place
   repeat = input(f"If you done, enter quit, or press any key to continue. ")
   if repeat.lower() == 'quit':
      active = False
name_place(places)
# Above the 2nd we actually finished the while loop just used the FN to print the msg, what if we want a FN participating all while loop?

def name_place(name,place):
   name = input(f"Enter your name please: ")
   place = input(f"Enter your favoriate dream vacation place: ")
   places[name] = place
   print(f"Hi {name.title()}, your favorite dream vacation place is {place.title()}.")
places={}
active = True
while active:
   name_place(name,place)
   repeat = input(f"If you done, enter quit, or press any key to continue. ")
   if repeat.lower() == 'quit':
      active = False

# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
# similar example as the printing example in textbook
# start the pizza with customer order
ordered_toppings = ['mushroom','pineapple','cheese']
finished_toppings = []
# simulate each topping until it is all done
# move each finished topping to the finished list
while ordered_toppings:
   current_topping = ordered_toppings.pop()
   print(f"{current_topping} is making now.")
   finished_toppings.append(current_topping)
# Display the finished toppings
for finished_topping in finished_toppings:
   print(finished_topping)

# Below we use functions 
def add_topping(ordered_toppings,finished_toppings=[]):
   '''start adding ordered toppings and move the added topping to finished topping list'''
   while ordered_toppings:
    current_topping = ordered_toppings.pop()
    print(f"{current_topping} is beding added now.")
    finished_toppings.append(current_topping)

def show(finished_toppings):
   '''display all added toppings'''
   print(f"\nThe added toppings are: ")
   for finished_topping in finished_toppings:
      print(finished_topping)

ordered_toppings = ['mushroom','pineapple','cheese']
finished_toppings = []
add_topping(ordered_toppings,finished_toppings)
show(finished_toppings)
# every function should have one specific job. The first function add toppings, and the second displays the completed toppings

# Preventing a Function from Modifying a List
# function_name(list_name[:])
# add_topping(ordered_toppings[:],finished_toppings)

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
 """Print the list of toppings that have been requested."""
 print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments: If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed last in the function definition
def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
    print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments. Attention to ** dictionary key-value pairs
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)

# Storing Your Functions in Modules
# module_name.function_name()
import pizza
pizza.make_pizza(12,'mushroom','cheese','pepperoni')

# Importing Specific Functions 
# from module_name import function_name
from pizza import make_pizza
make_pizza(16,'chesse')

# Using as to Give a Function an Alias
# from module_name import function_name as alias
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
# import module_name as mn
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
# from module_name import *
from pizza import *

