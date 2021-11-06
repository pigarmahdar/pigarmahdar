# 4.1 pizza questions
pizza = ['pepperoni', 'meatballs', 'vegetarian', 'olives']
for pizza in pizza:
	print("You really need to try " + pizza.title() + " because they're so yum!" + "\n")
	print("Have you tried this flavour?")

print("\nI really love pizza!")

# 4.2 counting to twenty
for value in range(1,21):
	print(value)
	
odd_numbers = list(range(1,20,2))
print(odd_numbers)
for value in range(1,20,2):
	print(value)

for value in range(3,30,3):
	print(value)

three = list(range(3,30,3))
print(three)

cube = [value**3 for value in range(1,11)]
print(cube)