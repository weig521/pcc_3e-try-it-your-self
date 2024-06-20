'''represent user including special user of admi and the privileges'''

class User:
    '''class user with first and last names and other attributes'''
    def __init__(self,first_name,last_name,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        '''Print user info'''
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, gender is {self.gender}.")

    def greet_user(self):
        '''print welcome message with their name'''
        print(f"Hi {self.first_name.title()} {self.last_name.title()}, welcome!")
    
    def increment_login_attempts(self):
        '''increase the login attempts by 1'''
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        '''Reset the login attempts to 0'''
        self.login_attempts = 0

class Privileges:
    '''privileges to be an administrator'''

    def __init__(self):
        '''initialize attributes'''
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        ''' print a message showing the admi privileges'''
        print(f"The admi privileges are: ")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    '''write a child class of User with new attribute'''

    def __init__(self, first_name, last_name, gender):
        '''initialize attributes of the parent class and its own attributes'''
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()