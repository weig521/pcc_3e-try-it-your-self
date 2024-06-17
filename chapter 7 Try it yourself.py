'''7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me 
see if I can find you a Subaru.”'''
make = input('What make of rental car do you prefer? ')
print(f"Let me see if I can find you a {make}")

'''7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print
a message saying they’ll have to wait for a table. Otherwise, report that their table is ready'''
num = int(input('How many people are in your dinner group please? '))
if num >8:
    print(f'I am sorry but you have to wait for a table, waiting time around 30 minutes.')
else:
    print('This way please, your table is ready.')

'''7-3. Multiples of Ten: Ask the user for a number, and then report whether thenumber is a multiple of 10 or not.'''
num0 = int(input('Please enter the number you want to know if it is a multiple of 10: '))
if num0 % 10 == 0:
    print(f'Yes, the number {num0} you entered is a multiple of 10.')
else:
    print(f'The number {num0} you entered is not a multiple of 10.')

'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza.'''
active = True
while active:
    topping = input('Please enter the topping you want to add on your pizza, or enter quit to finish. ')
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"You'll add {topping.title()} to your pizza. ")

'''7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.'''

while True:
    age = input('Please enter your age, when you done, enter quit to exit. ')
    if age.lower() == 'quit': # might be typo like qUit, Quit or what. There might be a typo which .lower is not quit, we will handle this in later chapter
        break
    if int(age) < 3: # remember to parse string to integer for numerical comparison
        print('The ticket if free.')
    elif int(age) <= 12:
        print(f"The ticket price is $10")
    else:
        print(f"The ticket price is $15.")

'''7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value'''
# break stmt to exit
age = ''
while age != 'quit':
    age = input('Please enter your age, when you done, enter quit to exit. ')
    if age.lower() != 'quit':
        age = int(age)
        if age < 3:
            print('The ticket if free.')
        elif age <= 12:
            print(f"The ticket price is $10")
        elif age > 12:
            print(f"The ticket price is $15.")

# active variable, and conditional test in 7-5
active = True
while active:
    age = input('Please enter your age, when you done, enter quit to exit. ')
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print('The ticket if free.')
        elif age <= 12:
            print(f"The ticket price is $10")
        elif age > 12:
            print(f"The ticket price is $15.")

'''7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.'''
count = 1
while count <= 5:
    print(count)


'''7-8. Deli: Make a list called sandwich_orders&fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.'''
sandwidwich_orders = ['club sandwich','chicken sandwich','beef sandwich']
finished_sandwiches = []
while sandwidwich_orders:
    finished_sandwich = sandwidwich_orders.pop()
    print(f"I made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)
print(finished_sandwiches)

'''7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.'''
sandwidwich_orders = [
    'club sandwich','chicken sandwich','beef sandwich',
    'pastrami','pastrami','pastrami'                      
                      ]
print(f"\n\tSorry, we run out of pastrami for today.")
while 'pastrami' in sandwidwich_orders:
    sandwidwich_orders.remove('pastrami')
print(sandwidwich_orders)

'''7-10. Dream Vacation: Write a program that polls users about their dream 
vacation. Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll.'''
responses = {}
response_active = True
while response_active:
    name = input(f"What is your name? ")
    response = input(f"What is your most dream vacation place? ")
    responses[name] = response

    repeat = input(f"Anyone else wants to share the information? yes/no: ")
    if repeat.lower() == 'no':
        response_active = False 
for name, response in responses.items():
    print(f"{name.title()} would like to {response.title()} most for vacation.")

