#Chapter 5 Exercises
#1. Person ####################################################
print("Exercise 1: Person")

person = {'first_name': 'Joaquin','last_name': 'Manly','age': 16,'city': 'Abu Dhabi'} #List of info

print(person['first_name']) #prints my first name
print(person['last_name']) #prints my last name
print(person['age']) #Prints my age
print(person['city']) #Print the city I live

#2. Glossary  ####################################################
print("\nExercise 2: Glossary")

glossary = {
    'if else': 'Chooses on which part of the code is going to be used depending on the situaton.', #The glossary
    'pop()': 'Can remove a variable from a list.',
    'lstrip': 'Removes the left part of the string.',
    'comments': 'a way to put a note inside the code without changing te code itself.',
    'Variables': ' is a number or a string of letters that is subject to change based on other parts of the code or data given to the application.',
    }
word = 'if else' # Prints the glossary
print(f"\n{word.title()}: {glossary[word]}")

word = 'pop()'
print(f"\n{word.title()}: {glossary[word]}")

word = 'lstrip'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comments'
print(f"\n{word.title()}: {glossary[word]}")

word = 'Variables'
print(f"\n{word.title()}: {glossary[word]}")

#3. Glossary 2 ####################################################
print("\nExercise 3: Glossary 2")

glossary = {
    'if else': 'Chooses on which part of the code is going to be used depending on the situaton.', #The glossary
    'pop()': 'Can remove a variable from a list.',
    'lstrip': 'Removes the left part of the string.',
    'comments': 'a way to put a note inside the code without changing te code itself.',
    'Variables': ' is a number or a string of letters that is subject to change based on other parts of the code or data given to the application.',
    'rstrip': 'Removes the right part of the string',
    'list' : 'are a series of variables that are all under a single name'
    }

for word, definition in glossary.items(): # Prints the whole glossary with a small code using a loop to repeat the code
    print(f"\n{word.title()}: {definition}")

#4. Rivers ####################################################
print("\nExercise 4: Rivers")

rivers = {
    'Yamuna': 'India', # Lists rivers
    'Nile': 'Africa',
    'Shinano': 'Japan',
    'Pasig': 'Philippines',
    'Ohio': 'US',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nRivers")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries: ")
for country in rivers.values():
    print(f"- {country.title()}")

#5. Pets #########################################################
print("\nExercise 5: Pets")

pets = []

pet = {
    'animal type': 'Cat', # First Pet
    'name': 'Cake pop',
    'owner': 'Joaquin',
    'weight': 12,
    'eats': 'Tuna',
}
pets.append(pet)

pet = {
    'animal type': 'Bird', # Second Pet
    'name': 'Iago',
    'owner': 'Jafar',
    'weight': 6,
    'eats': 'bread',
}
pets.append(pet)

pet = {
    'animal type': 'Dog', # Third pet
    'name': 'Pochita',
    'owner': 'Denji',
    'weight': 27,
    'eats': 'bread',
}
pets.append(pet)

for pet in pets: #Uses for loop to print all of it easily
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")