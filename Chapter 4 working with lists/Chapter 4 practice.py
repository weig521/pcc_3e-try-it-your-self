# for loop
cars = ['BMW','Honda','Toyota','Kia']
for car in cars:
    print(f'{car} is a make I like.')
print('They are all good car brands.')

for i in range(5):
    print(i) # ending number not included like the index of lists

numbers = list(range(5))
print(numbers)

evenNumbers = list(range(2,11,2))
print(evenNumbers)

cube = []
for i in range(1,11):
    cube.append(i**3)
print(cube)
# cube = [i**3 for i in range(1,11)] this is the same as above
min(cube)
max(cube)
sum(cube)

# Working with Part of a List
cube = [i**3 for i in range(1,11)]
print(cube)

print(cube[0:3]) # ending not included
print(cube[:3]) # omit the 0 if start from the beginning
print(cube[3:]) # similar as omitting 0 from beginning, omitting the last part gives us index 3 to the end
print(cube[-3:])

for i in cube[:3]:
    print(i)

# copying a list
a = [1,2,3,4,5]
b = a[:]
print(b)
b.append(6)
print(b)
print(a) # this is how it works. wrong way below:
c = [1,2,3]
d = c
print(d)
d.pop()
print(d)
print(c) # c is changed too. do not use this way, use slice copy

# Tuples: immutable list
dimensions = (200,50)
dimensions[0]
dimensions[1]

dimensions[0] = 150 # error msg occurs, tuples cannot change, it is immutable

a = (3,) # use comma to declare this is a tuple, if no comma, it would be a integer
type(a)



print('Original dimensions:')
for dimension in dimensions: 
    print(dimension)    # looping through all tuple is the same as list
dimensions = (150,50) # we can rewrite/reassign the whole variable to change the tuple
print('\n\tNew dimensions:')
for dimension in dimensions: 
    print(dimension)   