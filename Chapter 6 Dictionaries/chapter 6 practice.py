
'''A dictionary in Python is a collection of key-value pairs. Each key is connected to
a value, and you can use a key to access the value associated with that key. A
key’s value can be a number, a string, a list, or even another dictionary. In fact,
you can use any object that you can create in Python as a value in a dictionary.'''
alien_0 = {'color':'green','points':5} # create a dictionary, which is wrapped with braces {} , with : in there, seperated by ,
type(alien_0)
alien_0['color'] # to access the value associated with its key

# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary with students' scores
dict = {}
dict['adam'] = 87
dict['bob'] = 90
dict

# Modifying Values in a Dictionary
dict['adam'] = 97 # adam's score was input wrongly, now we correct it to 97
print(f'Score for student Adam is {dict['adam']}')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
 # assume only 3 speeds slow medium and fast, this would be the fast
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}") # alien_0 speed is medium, now it's on x_position 2

# Removing Key-Value Pairs
del dict['bob'] # like in list, deleted permanently
print(dict)

# Using get() to Access Values
# keyerror occurs when we requesting values with keys that not in the dict. we can use dictionary.get() to avoid error
alien_0 = {'color': 'green', 'speed': 'slow'}
alien_0.get('points', 'No point value assigned.') 
print(alien_0.get('points')) # return none if no second argument above

# Looping Through a Dictionary. Check the syntax and example below. add .items(), use i,j to represent the key value in dictionary
# for key, value in dict.items():
 #    print(key, value)
fav_languages = {
    'adam':'Python',
    'bob':'Java',
    'cathy':'C',
    'daviad':'C++'
}
for name, language in fav_languages.items():
    print(f"{name}'s favorite programming language is {language}.")

# Looping Through All the Keys in a Dictionary. the .keys() could be ommitted
for name in fav_languages.keys():
    print(name.title())

friends = ['adam','emma']
for name in fav_languages.keys():
    print(f'Hi {name.title()}')
    if name in friends:
        print(f"\tHi {name.title()}, I see that you love {fav_languages[name].title()}")
    else:
        print(f"\tHi {name.title()}, please take our poll.")

# Looping Through a Dictionary’s Keys in a Particular Order
# sorted() Python sort the keys first before the loop
for name in sorted(fav_languages.keys(),reverse = True):
    print(f"Hi {name.title()}, thank you for taking our poll.")

# Looping Through All Values in a Dictionary .values()
# use set() to avoid repeating
print(f'The mentioned languages are: ')
for v in set(fav_languages.values()):
    print(f"{v.title()}")

x = {5,7,7,8}
x # not ordered, not repeated elements

# Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)