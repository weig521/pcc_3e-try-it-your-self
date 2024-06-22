# A path is the exact location of a file or folder on a system. 
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

print(contents)
contents = path.read_text().rstrip() # now the last empty line is gone
print(contents)

# Relative and Absolute File Paths
# path = Path('text_files/filename.txt') 
# . A relative file path tells Python to look for a given location relative to the directory
# where the currently running program file is stored.suppose we need filename.txt in text_files
# which is in the cwd, use above code 

# Absolute file path tells Python exactly where the file is on your computer, regardless of where
# the program that’s being executed is stored. like below
# path = Path('/home/eric/data_files/text_files/filename.txt')

# Accessing a File’s Lines
lines = contents.splitlines()
for line in lines:
    print(line)
print(lines)

# Working with a File’s Contents
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)
print(len(pi_string))
# 10 decimals each line plus 3., we expect 32 for the len. it is 36 coz the whitespaces beginning of 2nd and 3rd line. 
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string)) # with the unwanted whitespaces stripped, we get the right  as the string length

# Large Files: One Million Digits
# below is the pi with  millon decimal places, same logic as above
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is Your Birthday Contained in Pi? 
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Writing to a File
# Writing a Single Line Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert 
# the data to string format first using the str() function.
from pathlib import Path
path = Path('programming.txt') # if no such a pre created file, python will create one for you
path.write_text("I love programming.") # in textbook it says no output for the write_text FN, acutally it returns the length of the wirtten text

# Writing Multiple Lines
from pathlib import Path

path = Path('programming.txt')
content = 'I love programming.\n'
content += 'I love creating new games.\n'
content += 'I love working with data.\n'
path.write_text(content)
# attention to write_text(): if no file yet, python create one for you; if file there already, the FN replace old content; it will save and close txt

# Exceptions
# A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised
# alice.py 
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text(encoding='utf-8') # FileNotFoundError occurs

from pathlib import Path
path = Path('nothere.txt')
try: 
    contents = path.read_text(encoding='utf-8') 
except FileNotFoundError:
    print(f"Sorry, file {path} is not found.")
else:
    print(contents) # replace nothere.txt with pi_digits.txt and try again. it will print contents since file exists

# Analyzing Text
from pathlib import Path
path = Path('alice.txt')
try:
 contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
 print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# Working with Multiple Files
# if we have multiple books we want to know their word counts accordingly, we could def a FN and use loop to do it
from pathlib import Path
def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.") # pass -- use pass to fail silently
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
# for one book alice, we do the next
path = Path('alice.txt')
count_words(path)
# for multiple books, see below
filenames = ['alice.txt', 'moby_dick.txt', 'siddhartha.txt','little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
# Using the try-except block in this example provides two significant advantages. 
#   ----We prevent our users from seeing a traceback
#   ----we let the program continue analyzing the texts it’s able to find (siddhartha in our case)

# E The JSON (JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a 
# common format used by many languages, including Python.
# number_writer.py
from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

# above is to write and save json doc, below is to import and use
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)
type(numbers)

# Saving and Reading User-Generated Data
# remember_me.py
from pathlib import Path
import json

username = input('What is your name? ')

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We will remember you, {username}!")

# greet_user.py
from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Wecome back, {username}!")

# above we ask a user to input his name and save it, then next time we 
# welcome him back. below is a better way to do it. If json file exists,
# we read and greet; else we record it
from pathlib import Path
import json
path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")


# Refactoring: process of improving the code by breaking it up into 
# a series of  functions that have specific jobs
from pathlib import Path
import json
def greet_user():
    '''Greet the user by name'''
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")
greet_user()
'''in this specific case, the greet_user() FN is good here. but it includes
too many tasks. What if we want to save name only, or load only? We may want
to refactor into smaller pieces with less or single function'''

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")
greet_user()

