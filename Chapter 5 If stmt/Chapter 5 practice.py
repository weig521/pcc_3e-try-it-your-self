cars = ['audi', 'bmW', 'subaru', 'toyOta'] # some brands/makes not typed correctly, like the bmW, toyOta, we want to print correctly
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#comparison
5 == 3
5 >= 3
5 <= 3 
5 != 3
(5 >=3) and (5<=3) 
(5 >=3) or (5<=3) 
5 >= (3 or 7)
5 >= (3 and 7)

'audi' in cars

user = 'john'
if 'Honda' not in cars:
    print(f'Sorry {user.title()}, Honda is not in our list.')

age = int(input('Enter your age please: '))
if age <= 4:
    price = 0
elif age <= 18:
    price = 12.5
else:
    price = 25
print(f'Your cost today is ${price}')

# Using if stmt in lists
# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print('Sorry, we run out of mushrooms.')
    else:
        print(f'Adding {requested_topping}')
print("\nFinished adding toppings.")

# Checking That a List Is Not Empty
requested_toppings = [] # bool([]) returns False, if requested toppings list is empty, the if-else stmt jumps to else since the if is false
if requested_toppings:
 for requested_topping in requested_toppings:
     print(f"Adding {requested_topping}.")
 print("\nFinished making your pizza!")
else:
 print("Are you sure you want a plain pizza?")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")