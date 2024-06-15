'''6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they
live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.'''
adam = {'first_name':'adam','last_name':'smith','age':18,'city':'tampa'}
adam['first_name']
adam['last_name']
adam.get('age')
adam.get('city')

'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think
of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even 
more fun, poll a few friends and get some actual data for your program.'''
favorite_numbers = {
    'adam':88,
    'bob':66,
    'cathy':100
    }
print(f"Adam's favorite number is {favorite_numbers['adam']}")
print(f"Bob's favorite number is {favorite_numbers['bob']}")
print(f"Cathy's favorite number is {favorite_numbers['cathy']}")

'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the 
word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each 
word-meaning pair in your output.'''
glossary = {
    'list':'A list is a collection of items in a particular order.',
    'tuple':'A tuple is kind of a list wrapped with parentheses instead of square brackets.',
    'dictionary':'A dictionary is a collection of key-value pairs',
    'float': 'Float is any number with a decimal point',
    'constant':'A constant is a variable whose value stays the same throughout the life of a program'
}
word = 'list'
print(f'{word}\n{glossary[word]}')

word = 'tuple'
print(f'{word}\n{glossary[word]}')

word = 'dictionary'
print(f'{word}\n{glossary[word]}')

word = 'float'
print(f'{word}\n{glossary[word]}')

word = 'constant'
print(f'{word}\n{glossary[word]}')

'''6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of
print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to
your glossary. When you run your program again, these new words and meanings should automatically be included in the output.'''
for i,j in glossary.items():
    print(f"{i.title()}: {j}")
glossary['boolean expression'] = 'A Boolean expression is another name for a conditional test.' 
glossary['boolean value'] = 'A Boolean value is either True or False'
glossary['zen of python'] = 'Listing of Python design principles and philosophies that are helpful in understanding and using the language.'
glossary['type'] = 'The type of a Python object determines what kind of object it is.'
glossary['string'] = 'A series of characters.'
for i,j in glossary.items():
    print(f"{i.title()}: {j}")

'''6-5. Rivers: Make a dictionary containing 3 major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'
• Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.'''
rivers = {
    'nile':'egypt',
    'yellow river':'china',
    'missouri river':'america'
    }
for i,j in rivers.items():
    print(f"{i.title()} runs through {j.title()}")
for i in rivers:
    print(i)
for j in set(rivers.values()):
    print(j)

''' 6-6. Polling: Use the code in favorite_languages.py (page 96). 
• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take the poll.'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
 }
names = ['jen','phil','alex','sofia']
for name in names:
    if name in favorite_languages.keys():
        print(f"Hi {name.title()}, thank you for taking the poll.")
    else:
        print(f"Hi {name.title()}, please take the poll.")

'''6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store
all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about
each person.'''
adam = {'first_name':'adam','last_name':'smith','age':18,'city':'tampa'}
bob = {'first_name':'bob','last_name':'green','age':19,'city':'clearwater'}
luke = {'first_name':'luke','last_name':'galler','age':23,'city':'orlando'}
people = [adam,bob,luke]
for i in people:
    print(f"{i['first_name'].title()} {i['last_name'].title()} who lives in {i['city'].title()} is {i['age']} years old.")

'''6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
owner’s name. Store them in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.'''
pet0 = {
    'kind':'cat',
    'owner':'bob'
    }
pet1 = {
    'kind':'dog',
    'owner':'david'
    }
pet2 = {
    'kind':'lion',
    'owner':'emma'
    }
pets = [pet0,pet1,pet2]
for pet in pets:
    print(f"The kind of this pet is a {pet['kind']} and its owner is {pet['owner'].title()}")

'''6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three
favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop 
through the dictionary, and print each person’s name and their favorite places.'''
favorite_places = {
    'Fiona':['new york','rome','beijing'],
    'greg':['Tokyo','Paris'],
    'henry':['dubai']
}
for name,places in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")

'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. Then print each 
person’s name along with their favorite numbers.'''
favorite_numbers = {
    'adam':[88,99],
    'bob':[66,88],
    'cathy':[100,1000,10000]
    }
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")
    
'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information 
about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s
dictionary should be something like country, population, and fact. Print the name of each and all of the information you have stored about it.'''
cities = {
    'new york':['america',30000000,'world economy center'],
    'beijing':['china',60000000,'capital of china'],
    'rome' : ['italy',40000000,'city of romance']
}
for city,facts in cities.items():
    print(f"City {city.title()}'s country, population, and fact are: ")
    for fact in facts:
        print(f"\t{fact}")