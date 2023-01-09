#Chapter 4 Exercises
#1. Alien Colors #1 ####################################################
print("Exercise 1: Alien Colors #1")

alien_color = input("Is the alien green, red or yellow?")

if alien_color == 'green': # If the alien is green the user gets a point
    print("You just earned 5 points!")

alien_color = input("Is the alien green, red or yellow?")

if alien_color == 'yellow':# If the alien is yellow the user gets a point
    print("You just earned 5 points!")

#2. Alien Colors #2 ####################################################
print("\nExercise 2: Alien Colors #2")

alien_color = input("Is the alien green, red or yellow?")

if alien_color == 'green': # If the alien is green the user gets a point
    print("You just earned 5 points!")
else:# If the alien is other than color green the user gets 10 points
    print("You just earned 10 points!")

alien_color = input("Is the alien green, red or yellow?")

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#3. Alien Colors #3 ####################################################
print("\nExercise 3: Alien Colors #3")

alien_color = 'red' 

if alien_color == 'red': # Gives points depending on what color the alien is
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'green'

if alien_color == 'red': # Gives points depending on what color the alien is
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'yellow'

if alien_color == 'red': # Gives points depending on what color the alien is
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

#4. Stages of Life####################################################
print("\nExercise 4: Stages of Life")

age = int(input("Input your age: "))

if age < 2: #If the age is smaller than 2 they are a baby
    print("You're a baby!")
elif age < 4: #If the age is smaller than 4 but equal or higher than 2 they are a baby
    print("You're a toddler!")
elif age < 13: #If the age is smaller than 13 but equal or higher than 4 they are a kid
    print("You're a kid!")
elif age < 20: #If the age is smaller than 20 but equal or higher than 13 they are a teenager
    print("You're a teenager!")
elif age < 65: #If the age is smaller than 65 but equal or higher than 20 they are an adult
    print("You're an adult!")
else: #If they are not not in the other choices they are an elder
    print("You're an elder!")

#5. Favorite Fruit####################################################
print("\nExercise 5: Favorite Fruit")

favorite_fruits = ['Banana', 'Mango', 'Melon'] #Favorite fruits

if 'Banana' in favorite_fruits:
    print("You really like Bananas!")
if 'Mango' in favorite_fruits:
    print("You really like Mango!")
if 'Watermelon' in favorite_fruits:
    print("You really like watermelon!") #Not included in the list so it will not be printed
if 'Melon' in favorite_fruits:
    print("You really like melons!") 
if 'Strawberries' in favorite_fruits:
    print("You really like Strawberries!") #Not included in the list so it will not be printed