# use input() function to collect user input info and assign it to a variable for further use. Input would be string 
name = input("If you share your name, we can personalize the messages you see. \nSo now what is your name? ")
print(f'Hello, {name.title()}')

# Using int() to Accept Numerical Input
year = int(input('What is your birth year? '))
current_year = 2024
age = current_year - year # if we didn't use the int(), the input year would be a string which cannot be used to do calculation
print(f"Your age is {age}.")
# below with if-else to determine and display msg if the user could vote
if age >= 18:
    print(f"Congrats, you are old enough to vote!")
else:
    print(f'Sorry, you are {18-age} years away to vote.')

# The Modulo Operator(%): which divides one number by another number and returns the remainder
7 % 3 # 7 divided by 3 equals to 2 with remainder 1, returns 1 here
7 // 3 # floor division, returns the full part which is 2 here 
7 ** 3 # exponentation 
7 + 3
7 - 3
7 * 3
7 / 3   # Here are all the commonly used arthmetic operators

# even or odd
number = int(input('Please enter the number you want to know whether it is even or odd: '))
if number % 2 == 0:
    print(f"\n\tThe number {number} is even.")
else:
    print(f"\n\tThe number {number} is odd.")

# Introducing while loop
# counting to 5. set count to 1, when count<6, run the code below: print the count, and then add 1 to count. On and on til count !<6
count = 1
while count < 6:
    print(count)
    count += 1

# Letting the User Choose When to Quit the program
# parrot.py 
msg = ''
while msg != 'Q':
    msg = input("\nTell me something, and I will repeat it back to you, and enter Q to quit: ")
    print(msg)
# it works but when user input Q, the program prints Q and then stop. if we dont want to show the Q, we can do below:
msg = ''
while msg != 'Q':
    msg = input("\nTell me something, and I will repeat it back to you, and enter Q to quit: ")
    if msg != 'Q':
        print(msg)

# flag: For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the
# entire program is active. This variable, called a flag, acts as a signal to the program.
active = True
while active:
    msg = input('Tell me something, I will repeat back to you. Enter Q to quit: ')
    if msg == "Q":
        active = False
    elif msg == 'q':
        active = False
    else:
        print(msg)
# what if the user messup with capical or lower case q? yes we can use msg.lower() == 'q', or we can use above or below, like two conditions. 
# either will make the active to False and cause the program to stop
active = True
while active:
    msg = input('Tell me something, I will repeat back to you. Enter Q to quit: ')
    if msg == ("Q" or "q"):
        active = False
    else:
        print(msg)

# Using break to Exit a Loop
# A loop that starts with while True 1 will run forever unless it reaches a break statement.
prompt = "\nPlease Enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Using continue in a Loop
#  counts from 1 to 10 but prints only the odd numbers in that range
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Avoiding Infinite Loops
# Every while loop needs a way to stop running so it won’t continue to run forever
# like above code, if we omit += 1, it would be a infinite loop
current_number = 1
while current_number < 10:
    # current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# use Ctrl C to stop or simply close the terminal window 

# Using a while Loop with Lists and Dictionaries
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print(f"\n\tThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
The confusing part of above example to me is: while unconfirmed_users:
try bool([]), we can see it returns a false. The empty list bool value is false,
so when the list is not empty yet, the while loop continues. to get it easier:

while len(unconfirmed_users) != 0:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)

it means when the uncofirmed users list is not empty yet, while loop continues
'''

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
new_pets = []
for pet in pets:
    if pet.lower() != 'dog':
        new_pets.append(pet)
print(new_pets)

for pet in pets:
    if pet.lower() == 'dog':
        pets.remove(pet)
print(new_pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input
# mountain.py start with an empty dictionary to store data
responses = {}
# set a flag to indicate the polling is active
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to clim someday most? ')

    #store them in the dictionary
    responses[name] = response
    # find if anyone elase is going to take the poll
    repeat = input('Would you like to let another person respond?(yes/no) ')
    if repeat.lower() == 'no':
        polling_active = False
print("\n--- Poll Results: ---")
for i,j in responses.items():
    print(f"{i.title()} would like to clim {j.title()} most.")