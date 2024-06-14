current_year = 2024
first_name = input('Please enter your first name: ').title()
last_name = input('Please enter your last name: ').title()
year = int(input('Please enter your birth year: '))
age = current_year - year
print(f"Your name is {first_name} {last_name} and your age is {age}.")

# whitespace Tap
print('\tHello')
# whitespace newline
print('Python\nC\nJava\nJS')

# Removing whitespace
msg = 'Python ' # attention, it is Python ended with a space
msg.rstrip() # the space stripped. rstrip() right strip, strip the space on the right end
msg # as we see, the msg still has the space at the end, so we need to assign the stripped value to the variable msg
msg = msg.rstrip()
msg # Now msg varable has Python only without space at the end

message = ' Python  '
message.lstrip() # left strip
message.rstrip() # right strip no matter how many spaces 
message.strip() # strip both left and right

# Removing prefix/suffix
google_url = 'https://google.com.cn'
google_url.removeprefix('https://')
google_url.removesuffix('.cn')

# apostrophe use in double quotes
print("I like Paul's, especially its fries.") # if use single quote with apostrophe, error occurs

0.2+.1 # not 0.3 but 0.300000004 check it out
4/2 # even full division of two integers get flots
universeAge = 14_000_000_000 # we can use underscore in numbers to inrese readability, python doesnt read or store the _
print(universeAge)

x = y = z = 100 # multiple assignment 
X,Y,Z = 10,15,20
print(x,X)