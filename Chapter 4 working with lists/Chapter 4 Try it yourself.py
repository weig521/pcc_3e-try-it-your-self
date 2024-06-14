''' 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name
 of each pizza. 
 • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should
have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as I really love pizza!'''
pizzas = ['Triple meat','Double Cheese','Pepperoni']
for pizza in pizzas:
    print(f'I like {pizza} pizza')
'''4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then
 use a for loop to print out the name of each animal. 
 • Modify your program to print a statement about each animal, such as A dog would make a great pet.
 • Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals 
   would make a great pet! '''
animals = ['dog','cat','pig']
for animal in animals:
    print(animal)
for animal in animals:
    print(f'{animal} is a mammal with four legs.')

for animal in animals:
    print(f'{animal} is a mammal with four legs.')
print('Any of these animals would make a great pet.')

# 4-3 Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for num in range(1,21):
    print(num)
# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too
#  long, stop it by pressing CTRL-C or by closing the output window.)
numbers = list(range(1,1000001))
len(numbers)
# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts 
# at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
min(numbers)
max(numbers)
sum(numbers)
# 4-6. Odd Numbers: Use the third argument of range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
oddNumbers = list(range(1,21,2))
print(oddNumbers)
# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
nums = [i*3 for i in range(1,11)]
for num in nums:
    print(num)
# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first
# 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
cubes = [i**3 for i in range(1,11)]
for cube in cubes:
    print(cube)
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes = [i**3 for i in range(1,11)]

''' 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list. '''
cubes = [i**3 for i in range(1,11)]
print(f'The first three items in the list are: {cube[:3]}')
print(f'Three items from the middle of the list are: {cube[4:7]}')
print(f'The last three items in the list are: {cube[-3:]}')

''' 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the 
message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate 
list. '''
pizzas = ['Triple meat','Double Cheese','Pepperoni']
friend_pizzas = pizzas[:]
pizzas.insert(3,'Cheese')
friend_pizzas.append('Mushroom')
print(f'My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
'''4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of 
foods.py, and write two for loops to print each list of foods. '''
myFood = ['Pizza','Pasta','Cheeseberg']
friendFood = myFood[:]

myFood.append('Fries')
friendFood.append('Subway')

print('My favorite food are: ')
for food in myFood:
    print(food)
print("My friend's favorite food are: ")
for food in friendFood:
    print(food)

''' 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the change.
• The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop
  to print each of the items on the revised menu.'''
foods = ('beef','chicken','rice','noodle','deseart')
for food in foods:
    print(food)
foods[0] = 'fish' #Python rejects to the change
foods = ('beef','chicken','shrimp','pasta','deseart')
for food in foods:
    print(food)

