'''10-1. Learning Python: Open a blank file in your text editor and write a few lines
summarizing what you’ve learned about Python so far. Start each line with the
phrase In Python you can. . . . Save the file as learning_python.txt in the same
directory as your exercises from this chapter. Write a program that reads the file
and prints what you wrote two times: print the contents once by reading in the
entire file, and once by storing the lines in a list and then looping over each line'''
from pathlib import Path

# read the file and print the content
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

# split content into lines, the lines would be a list doc, loop to print each line
lines = contents.splitlines()
for line in lines:
    print(line)

'''10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.'''
for line in lines:
    print(line.lower().replace('python','C')) # I input python 2nd line. .lower() could solve this 

'''10-3. Simpler Code: The program file_reader.py in this section uses a temporary
variable, lines, to show how splitlines() works. You can skip the temporary
variable and loop directly over the list that splitlines() returns:
for line in contents.splitlines():
Remove the temporary variable from each of the programs in this section,
to make them more concise.'''
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
    print(line.lower().replace('python','Java'))

'''10-4. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt'''
from pathlib import Path

path = Path('guest.txt')
name = input('Please enter your name: ')
path.write_text(name.title())

'''10-5. Guest Book: Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file.'''
from pathlib import Path
path = Path('guest_book.txt')

active = True
content = ''
while active:
    name = input('Please enter your name: ')
    content += (name.title()+'\n')
    repeat = input('Enter quit to exit or press any key to continue: ')
    if repeat.lower() == 'quit':
        active = False
path.write_text(content)

'''10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.'''
num_1 = input(f"Please enter the first integer: ")
num_2 = input(f"Please enter the second integer: ")
try:
    sum = int(num_1) + int(num_2)
except ValueError:
    print('Sorry, at least one input is not a number.')
else:
    print(f"The sum of your two entered numbers are: {sum}.")

'''10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.'''

active = True
while active:
    num_1 = input(f"Please enter the first integer: ")
    num_2 = input(f"Please enter the second integer: ")
    try:
        sum = int(num_1) + int(num_2)
    except ValueError:
        print('Sorry, at least one input is not a number.')
    else:
        print(f"The sum of your two entered numbers are: {sum}.")
    repeat = input(f"Please enter quit to exit or any key to continue. ")
    if repeat.lower() == 'quit':
        active = False

'''10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block
executes properly.'''
from pathlib import Path

cat_path = Path('cats.txt')
dog_path = Path('dogs.txt')
paths = [cat_path, dog_path]
for path in paths:
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Please make sure you have the corrent working directory.")
    else:
        print(contents.title())

'''10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail
silently if either file is missing.'''
for path in paths:
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contents.title())

'''10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org) and find
a few texts you’d like to analyze. Download the text files for these works, or
copy the raw text from your browser into a text file on your computer'''
# I cannot open the webpage, the text I used is the "I have a dream" speech. 49 the/The** and 31 the/The space.
from pathlib import Path
path = Path('I have a dream.txt')
lines = path.read_text().splitlines()
speech = ''
for line in lines:
    speech += line
speech.lower().count('the')
speech.lower().count('the ')

'''10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your 
favorite number! It’s _____.”'''
from pathlib import Path
import json

path = Path("favorite number.json")
fav_number = input("Please enter your favorite number: ")
contents = json.dumps(fav_number)
path.write_text(contents)


from pathlib import Path
import json

path = Path('favorite number.json')
contents = path.read_text()
fav_number = json.loads(contents)
print(f"I know your favorite number! It's {fav_number}.")

'''10-12. Favorite Number Remembered: Combine the two programs you wrote in
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works'''
from pathlib import Path
import json

path = Path('favorite number.json')
if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"I know your favorite number! It's {fav_number}.")
else:
    fav_number = input("Please enter your favorite number: ")
    contents = json.dumps(fav_number)
    path.write_text(contents)

'''10-13. User Dictionary: The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.'''
from pathlib import Path
import json

dict = {}
first_name = input(f"What is your first name? ")
last_name = input(f"Waht is your last name? ")
gender = input(f"What is your gender? ")
dict['first_name'] = first_name
dict['last_name'] = last_name
dict['gender'] = gender

path = Path('user info.json')
contents = json.dumps(dict)
path.write_text(contents)

from pathlib import Path
import json

path = Path('user info.json')
contents = path.read_text()
dict = json.loads(contents)
for i,j in dict.items():
    print(f"The user's {i} is {j.title()}.")


'''10-14. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who last
used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.'''
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
        answer = input(f"Are you {username}? yes/no: ")
        if answer.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = input("What is your name? ")
            contents = json.dumps(username)
            path.write_text(contents)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")
greet_user()

