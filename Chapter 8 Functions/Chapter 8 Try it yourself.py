'''8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about 
in this chapter. Call the function, and make sure the message displays correctly.'''
def display_message():
    '''The FN tells that I learnt FN this chapter'''
    print(f"I learnt function in this chapter.")
display_message()

'''8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.'''
def favorite_book(title):
    '''FN that take an argument as parameter to tell the favorite book'''
    print(f"{title.title()} is my favorite book.")
favorite_book('Rich dad, poor dad')

''' 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''
def make_shirt(size,msg):
    '''Display message summarizing the size of shirt and msg printed on it'''
    print(f"The shirt size is {size}, and the message to be printed on the shirt is {msg}.")
make_shirt('L','Love')
make_shirt(msg='Love',size='L')

'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.'''
def make_shirt(size='L',msg='I love Python'):
    '''Display message summarizing the size(default L) of shirt and msg (default I love Python) printed on it'''
    print(f"The shirt size is {size}, and the message to be printed on the shirt is {msg}.")
make_shirt('M')
make_shirt()
make_shirt('S','Python is my love')

'''8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned.'''

# Right below is the function, if we don't use the while loop, we can simply put city and country names in the called FN parameters
def city_country(city,country):
    print(f"{city.title()}, {country.title()}")

dict = {}
active = True
while active:
    city = input(f"Please enter a city name: ")
    country = input(f"Please enter the Country the city belongs to: ")
    dict[city] = country
    city_country(city,country)
    repeat = input(f"If you done, enter quit, else press any key to continue: ")
    if repeat == 'quit':
        active = False
print(dict)  # creating a dictionary and saving values is not required, but it is useful

'''8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.'''
def make_album(name,title):
    dict = {}
    dict['artist'] = name.title()
    dict['Album title'] = title.title()
    return dict
make_album('Jay Joe','Qilixiang')
make_album('Taylor Swift','Love story')
make_album('Ali','Endless fighting')

def make_album(name,title,number=''):
    dict = {}
    dict['artist'] = name.title()
    dict['Album title'] = title.title()
    if number: 
        dict['number of songs'] = number
    return dict
make_album('Taylor Swift','Love story',10)
make_album('Jay Joe','Qilixiang')

'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop'''
def make_album(name,title):
    '''build a FN to display a dictionary with artist name and album title'''
    dict = {}
    dict['artist'] = name.title()
    dict['Album title'] = title.title()
    return dict
artist = {}
active = True
while active:
    name = input(f"Please enter the artist's name: ")
    title = input(f"Please enter the album title of the artist: ")
    artist[name]=title
    make_album(name,title)
    repeat = input(f"When you done, enter quit, or press any key to continue: ")
    if repeat == 'quit':
        active = False
print(artist) # user input is stored in a dictionary artist too

'''8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.'''
msgs = ['I love Python','I love C','I love Java']
def show_messages(msgs):
    ''' print all messages in the parameter list'''
    for msg in msgs:
        print(msg)
show_messages(msgs)

'''8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.'''
messages = ['I love Python','I love C','I love Java']
sent_messages = []
def send_messages(messages,sent_messages=[]):
    while messages:
        current_message = messages.pop()
        print(f"{current_message}")
        sent_messages.append(current_message)
send_messages(messages,sent_messages)
print(messages)
print(sent_messages)

'''8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.'''
messages = ['I love Python','I love C','I love Java']
sent_messages = []
send_messages(messages[:],sent_messages)
print(messages)
print(sent_messages)

'''8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich 
that’s being ordered. Call the function three times, using a different number of arguments each time.'''
def sandwiches(*items):
    ''' Display all the items customer wants on the sandwich'''
    print(f"\nThe items you want on the sandwich as below: ")
    for item in items:
        print(item)
sandwiches('meat')
sandwiches('meat','beef','olives')
sandwiches('tomato','olive','spinach')

'''8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.'''
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Da', 'Ge',
 location='Tampa',
 field='Business Analytics',
 gender = 'male')
print(user_profile)

'''8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and 
a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other
name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly'''
def car_info(manufacturer,model,**car_info):
    '''build a dictionary containing all we know about a car'''
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car_info('subaru','forester',
         cylinder = 4,
         door = 4,
         trim = 2.5)

'''8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.'''
# save the .py under the same folder, we have many diff ways to import
# plz check the pizza.py example in chapter 8 practice for this

'''8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *'''
import pizza
from pizza import make_pizza
from pizza import make_pizza as mp
import pizza as p
from pizza import *

'''8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.'''
# I did realize that I forget the docstring right under the def line; and did not notice no space before and after the parameter =