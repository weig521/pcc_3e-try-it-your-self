''' page 16 TRY IT YOURSELF
Write a separate program to accomplish each of these exercises. Save each program with a filename that follows standard Python conventions, using lowercase
letters and underscores, such as simple_message.py and simple_messages.py.
2-1. Simple Message: Assign a message to a variable, and then print that
message.
2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new
message.'''
# 2-1
message = 'Good morning!'
print(message)
#2-2
message = 'Good morning!'
print(message)

message = 'Good afternoon!'
print(message)

# 2-3 Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
name = 'John'
print('Hello',name, 'would you like to learn some Python today?')

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case
name = 'John'
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something 
# like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
print('Mathematician Clive Humby mentioned, "Data is the new oil. Like oil, data is valuable, but if unrefined it cannot really be used."')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then 
# compose your message and represent it with a new variable called message. Print your message.
famous_person = 'Clive Humby'
message = f'Mathmatician {famous_person} once said, "Data is the new oil. Like oil, data is valuable, but if unrefined it cannot really be used."'
print(message)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
personName = "\tIvan\n"
print(personName)
print(personName.lstrip())
print(personName.rstrip())
print(personName.strip())

#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable 
# called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your
#  operations in print() calls to see the results. You should create four lines that look like this: print(5+3). Your output should be four lines, 
# with the number 8 appearing once on each line.
print(4+4)
print(9-1)
print(4*2)
print(16/2)

# 2-10. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite
#  number. Print that message
fav_number = 8
msg = f'{fav_number} is my favoriate number.'
print(msg)

'''2-11 comments. Use """""" for paragraph comment, 
and # for line comment as above and now.'''