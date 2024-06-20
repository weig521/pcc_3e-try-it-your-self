'''Represent a restaurant's name, cuisine type, and served customers'''
class Restaurant:
    '''create restaurant class with name and cuisine type'''
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        '''Display a msg about the name and cuisine type of restaurant'''
        print(f"The name of the restaurant is {self.name} and the cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        '''Indicate that the restaurant is open'''
        print(f"The restaurant is open now.")
    def set_number_served(self,number):
        '''to set the number of served customers'''
        self.number_served = number
    def increment_number_served(self,count):
        '''display the increased count to the served customers'''
        self.number_served =+ count