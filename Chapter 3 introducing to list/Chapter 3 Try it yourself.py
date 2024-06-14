# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one
# at a time.
names = ['Adam','Bob','Charlie','David']
names[0]
names[1]
names[2]
names[3]
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text 
# of each message should be the same, but each message should be personalized with the person’s name.
#for i in range(len(names)):
#    print(f'{names[i]}, how are you today?')
print(f'{names[0]}, how are you today?')
print(f'{names[1]}, how are you today?')
print(f'{names[2]}, how are you today?')
print(f'{names[3]}, how are you today?')
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
cars = ['Honda','Toyota','Subaru']
print(f'I would like to own a {cars[0]} SUV.')
print(f'I would like to own a {cars[1]} SUV.')
print(f'I would like to own a {cars[2]} SUV.')

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people
#  you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guestList = ['Adam','Bob','Charlie']
print(f'Dear {guestList[0].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[1].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[2].title()}, please come to my house for dinner coming Friday, June 15 2024.')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll 
# have to think of someone else to invite. 
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.
unattending_guest = guestList.pop(0)
print(f'{unattending_guest} cannot make it for the Friday dinner')
guestList.insert(0,'Amy')
print(f'Dear {guestList[0].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[1].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[2].title()}, please come to my house for dinner coming Friday, June 15 2024.')

'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list'''
print(f'Dear {guestList[0].title()}, I found a bigger table and more guests will be coming. See you Friday.')
print(f'Dear {guestList[1].title()}, I found a bigger table and more guests will be coming. See you Friday.')
print(f'Dear {guestList[2].title()}, I found a bigger table and more guests will be coming. See you Friday.')
guestList.insert(0,'Aming')
guestList.insert(2,'Cathy')
guestList.append('Emma')
print(f'Dear {guestList[0].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[1].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[2].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[3].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[4].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[5].title()}, please come to my house for dinner coming Friday, June 15 2024.')

""" 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only 
two guests. 
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
 a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at 
the end of your program."""
print('Sorry, only two guests will be invited to dinner the coming Friday, June 15 2024.')
popped = guestList.pop()
print(f'Dear {popped.title()}, sorry to inform you that the Friday dinner is canclled due to unexpected situation.')
popped = guestList.pop()
print(f'Dear {popped.title()}, sorry to inform you that the Friday dinner is canclled due to unexpected situation.')
popped = guestList.pop()
print(f'Dear {popped.title()}, sorry to inform you that the Friday dinner is canclled due to unexpected situation.')
popped = guestList.pop()
print(f'Dear {popped.title()}, sorry to inform you that the Friday dinner is canclled due to unexpected situation.')

print(f'Dear {guestList[0].title()}, please come to my house for dinner coming Friday, June 15 2024.')
print(f'Dear {guestList[1].title()}, please come to my house for dinner coming Friday, June 15 2024.')

del guestList[0] #if we remove the first element first, then only one element left in the list. We use [0] in next del stmt too
del guestList[0] # if we use [1], we forget the dynamic rule, attention to this
print(guestList)

''' 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed. '''
places = ['Rome','Beijing','Paris','Tokyo','Bali']
print(places)
sorted(places) # change the order into alphabetical order but doesn't affect the original list
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

'''3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the
 number of people you’re inviting to dinner.'''
guestList = ['Adam','Bob','Charlie'] # here is the guest list in 3-4
len(guestList)
print(f'{len(guestList)} guests will be invited to dinner.')

''' 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, 
languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this
 chapter at least once '''
seasons = ['Spring','Summer','Fall','Winnter']
print(f'There are {len(seasons)} seasons in a year.')
sorted(seasons)
sorted(seasons,reverse = True)
seasons.sort()
print(seasons)
seasons.sort(reverse = True)
print(seasons) 
# Then I realize winter is a typo, to correct it, I can
seasons.remove('Winnter') # or del seasons(0) or seasons.pop(0)
seasons.append('Winter') # now add the correct Winter in the list
print(seasons) # Oh no, the position changed
seasons.pop()
seasons.insert(0,'Winter')
print(seasons) # we are good now
# Or to make it easy, just use: seasons[0] = 'Winter'

''' 3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one
 of your programs to produce an index error. Make sure you correct the error before closing the program.'''
len(seasons)
seasons[4] # 4 items in seasons list, we want the forth one but forgot to -1, index error occurs