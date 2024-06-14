'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each
test. Your code should look something like this: 
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.'''
pet = 'puppy'
skills = ['run','bark']
print("Is pet == 'puppy'? I predict True.")
print(pet == 'puppy')
print("\nIs pet == 'kitten'? I predict False.")
print(pet == 'kitten')
print('Is the name length of the pet 5? I predict True')
print(len(pet) == 5)
print('Is the name length of the pet longer than 5? I predict False')
print(len(pet) > 5)
print('Is the name length of the pet no greater than 5? I predict True')
print(len(pet) <= 5)
print('Is the name length of the pet no greater than 4? I predict False')
print(len(pet) <= 4)
print('Does the pet swim? I predict False')
print('swim' in skills)
print('Does the pet run? I predict True')
print('run' in skills)
print('Does the pet bark, I predict True')
print('bark' in skills)
print('Does the pet fly? I predict False')
print('fly' in skills)

'''2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests
and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''
cars = ['audi','bmw','honda','toyota']
scores = [75,77,80,85]
for car in cars:
    if car.lower() == 'bmw':
        print(car)
scores[0] == 75
scores[1] !=77
scores[2] >= 80
scores[3] <= 80
(scores[0] == 75) and (scores[1] !=77)
(scores[0] == 75) or (scores[1] !=77)

'audi' in cars
'Honda' not in cars
'Honda'.lower() not in cars

'''5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 
'yellow', or 'red'. • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5
points. • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)'''
alien_color = 'green'
if alien_color == 'green':
    print('Congrats, you just earned 5 points.')

alien_color = 'yellow'
if alien_color == 'green':
    print('Congrats, you just earned 5 points.')

'''5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.'''
alien_color = 'green'
if alien_color == 'green':
    print('Congrats, you just earned 5 points for shooting the green alien.')
else:
    print('Congrats, you just earned 10 points for shooting the alien.')

alien_color = 'yellow'
if alien_color == 'green':
    print('Congrats, you just earned 5 points for shooting the green alien.')
else:
    print('Congrats, you just earned 10 points for shooting the alien.')

'''5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.'''
alien_color = 'yellow'
alien_color = 'green'
alien_color = 'red'

if alien_color == 'green':
    print('Congrats, you just earned 5 points')
elif alien_color == 'yellow':
    print('Congrats, you just earned 10 points')
else:
    print('Congrats, you just earned 15 points')

'''5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder'''
age = int(input('Please enter the age of the person:')) # input will be introduced later, you can assign any integer to age and run the program
if age < 2:
    print(f'A person at age {age} is a baby.')
elif age < 4:
    print(f'A person at age {age} is a toddler.')
elif age < 13:
    print(f'A person at age {age} is a kid.')
elif age < 20:
    print(f'A person at age {age} is a teenager.')
elif age < 65:
    print(f'A person at age {age} is an adult.')
else:
    print(f'A person at age {age} is an elder.')

'''5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in
your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should
print a statement, such as You really like bananas!'''
favorite_fruits = ['apple','watermelon','orange']
if 'apple' in favorite_fruits:
    print('I really like apple.')
if 'watermelon' in favorite_fruits:
    print('I really like watermelon.')
if 'orange' in favorite_fruits:
    print('I really like orange.')
if 'banana' in favorite_fruits:
    print('I really like banana.')
if 'strawberry' in favorite_fruits:
    print('I really like strawberry.')

'''5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting
to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.'''
usernames = ['admin','adam','bob','charlie','david']
for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username}, welcome back.')
''' 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.'''
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {username}, welcome back.')
else:
    print('We need to find some users!')

'''5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to 
  enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy
  of current_users containing the lowercase versions of all existing users.)'''
current_users = ['Adam','Bob','Charlie','David','Emma']
current_users_copy = []
for i in current_users:
    current_users_copy.append(i.lower())
print(current_users_copy)
new_users = ['aby','bob','cathy','doug','emma']
for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f'{new_user} has been taken, please pick another username.')

'''5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
8th 9th", and each result should be on a separate line.'''
numbers = list(range(1,10))
for number in numbers:
    print(number)
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')















