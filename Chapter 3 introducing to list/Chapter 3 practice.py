bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title()) # index, start with 0
print(bicycles[-1]) # use index -1 for the last element of the list, similar as -2,-3
print(bicycles[1:3]) # including starting slice but not the ending
print(f'{bicycles[-2].title()} is my favoriate bycicle brand.')

cars = ['Honda','Toyota','Subaru']
# Modifying, Adding, and Removing Elements
cars[0] = 'BMW'
print(cars) # first element of Honda is now BMW. Modifying

cars.append('Jetta') # appending an element to the end of the list
print(cars)
cars.insert(0,'Volvo') # insert a new eleemnt at specific position
print(cars)

del cars[0] #del FN, volvo brand removed. Can no longer access the removed element
print(cars)

popped_car = cars.pop() # remove the last element of the list but we can still access it for further use
print(cars)
print(popped_car)

first_owned = cars.pop(0)
print(cars)
print(first_owned)

cars.remove('Subaru') # remove an element with its value. Removes the first one if there are multiple same values
print(cars)

# Organizing a list
cars = ['BMW','Honda','Toyota','Subaru','Kia']
cars.sort() # sorted list will replace the old list permanently
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['BMW','Honda','Toyota','Subaru','Kia']
sorted(cars) # see the diff, sorted() doesn't affect the order of original list
print(cars)
sorted(cars,reverse=True)

cars.reverse() # reverse the order of the list permanently
cars

len(cars) # to find the length of the list, how many elements in the list