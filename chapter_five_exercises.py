alien_colour = ['green']
if 'green' in alien_colour:
	print("Yay! You just scored 5 points!")

alien_colour = ['green','yellow']
if 'green' in alien_colour:
	print("Yay! You just scored 5 points!")

alien_colour = ['blue','yellow']
if 'green' in alien_colour:
	print("Yay! You just scored 5 points!")
else:
	print("Nice! You scored 10 points!")

print("\n5.5 Alien Colours #3")
alien_colour = 'green'
if 'green' in alien_colour:
	score = 5
elif 'yellow' in alien_colour:
	score = 10
elif 'red' in alien_colour:
	score = 15

print("You scored " + str(score) + " points!")

alien_colour = 'yellow'
if 'green' in alien_colour:
	score = 5
elif 'yellow' in alien_colour:
	score = 10
elif 'red' in alien_colour:
	score = 15

print("You scored " + str(score) + " points!")

alien_colour = 'red'
if 'green' in alien_colour:
	score = 5
elif 'yellow' in alien_colour:
	score = 10
elif 'red' in alien_colour:
	score = 15

print("You scored " + str(score) + " points!")

print("\n5.6 Stages of life")
age = 15
if age < 2:
 	print("You're a baby")
elif age < 4:
 	print("You're a toddler")
elif age < 13:
 	print("Wow you're still a kid")
elif age < 20:
 	print("You're a teenager ew gross")
elif age < 65:
 	print("Congratulations you're officially an adult")
elif age > 65:
 	print("Oh no, you're getting old")

print("\n5.7 Favourite Fruits")
favourite_fruits = ['rambutan', 'mango', 'pineapple', 'oranges']

if 'strawberry' in favourite_fruits:
	print("You really like strawberries!")
if 'mango' in favourite_fruits:
	print("You really like mangoes!")
if 'durian' in favourite_fruits:
	print("You really like durian!")
if 'oranges' in favourite_fruits:
	print("You really like oranges!")
if 'rambutan' in favourite_fruits:
	print("You really like rambutan!")

print("\nUsing if statement with lists")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toppings in requested_toppings:
	print("Adding " + requested_toppings + ".")

print("\nFinished making your pizza!")

# Using multiple lists
print('\nUsing Multiple Lists')

available_toppings = ['mushrooms', 'olives','green peppers','pepperoni','pineapple','extra cheese']

requested_topppings = ['mushrooms','french fries','extra cheese']

for requested_topppings in requested_topppings:
	if requested_topppings in available_toppings:
		print("Adding " + requested_topppings + ".")
	else:
		print("Sorry, we don't have " + requested_topppings + ".")

print("\nFinished making your pizza!")

# 5.8 Hello Admin

website_users = ['admin','pottasy','anijava','maryjane','sugabts','yammonation']

if website_users:
	for website_users in website_users:
		if 'admin' in website_users:
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello "+ website_users + ", thank you for logging in again.")
else:
	print("We need to find more users!")		

# 5.10 checking usernames
current_users = ['admin','pottasy','anijava','maryjane','sugabts','yammonation']

new_users = ['jimin','pottasy','anijava','taehyun']

for new_users in new_users:
	if new_users in current_users:
		print("Sorry " + new_users + ", please enter a new username")
	else:
		print("Thank you " + new_users + ", the username is available. Welcome!")
