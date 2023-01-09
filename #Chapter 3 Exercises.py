#Chapter 3 Exercises
#1. Name##################################################################
print("Exercise 1: Names")
names = ["Sameer", "Rosver", "Rhodge"] #Names of friends
print(names[0]) #Printing the names
print(names[1])
print(names[2])

#2. Greetings#############################################################
print("\nExercise 2: Greetings")
names = ["Sameer", "Rosver", "Rhodge"] #Names of friends
msg = (f"Can you help me with this game {names[0].title()}?")
print(msg)
msg = (f"What did you think of the new chapter {names[1].title()}?")
print(msg)
msg = (f"You want to play Valorant {names[2].title()}?")
print(msg)

#3. Your Own List#########################################################
print("\nExercise 3: Your Own List ")
brand = ["Dodge Charger", "Ford F-150","xsr900"] #Names of vehicle models
transpo = ["car", "truck", "motorcycle"] #The type of vehicles
msg = (f"I want to own a {brand[0]} {transpo[0]}.")
print(msg)
msg = (f"I want to own a {brand[1]} {transpo[1]}.")
print(msg)
msg = (f"I want to own a {brand[2]} {transpo[2]}.") 
print(msg)

#4. Guest List###########################################################
print("\nExercise 4: Guest List")
guests = ["Kevin Hart", "Ryan Reynolds","Jim Carrey"] #Favorite Actors
name = guests[0].title()
print(f"{name}, I'm inviting you to dinner.") #Invites them to dinner
name = guests[1].title()
print(f"{name}, I'm inviting you to dinner.")
name = guests[2].title()
print(f"{name}, I'm inviting you to dinner.")

#5. Change Change Guest List####################################################
print("\nExercise 5: Change Guest List")
guests = ["Kevin Hart", "Ryan Reynolds","Jim Carrey"] #Favorite Actors

name = guests[0].title() #Original invites
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[2]) # Removes Jim Carrey
guests.insert(1, 'Dwayne Johnson') # Adds Dwayne Johnson

name = guests[0].title() #New list
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")


########################################

print("\nExercise 6: Shrinking Guest List")
print("    ")
guests = ['Beam', 'Galgali', 'Princi','Kobeni','Himeno'] 

name = guests[0].title()
print(f"{name}, you are invited to dinner this evening.")

name = guests[1].title()
print(f"{name}, you are invited to dinner this evening.")

name = guests[2].title()
print(f"{name}, you are invited to dinner this evening.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to the party.")

del(guests[1])
guests.insert(1, 'Kishibe')

name = guests[0].title()
print(f"\n{name}, you are invited to join the party later this evening.") # Invites them to dinner

name = guests[1].title()
print(f"{name}, you are invited to join the party later this evening.")

name = guests[2].title()
print(f"{name}, you are invited to join the party later this evening.")

print("\nSorry, I can only invite two people to dinner.")

name = guests.pop() # Removes their names
print(f"Sorry, {name.title()} there is no room at the dinner table.")

name = guests.pop()
print(f"Sorry, {name.title()} there is no room at the dinner table.")

name = guests.pop()
print(f"Sorry, {name.title()} there is no room at the dinner table.")

name = guests[0].title()
print(f"{name}, please come to the party.")

name = guests[1].title()
print(f"{name}, please come to the party.")

del(guests[0])
del(guests[0])

print(guests)
print("    ")
print("\nExercise 7: Seeing the World")
print("    ")
world = ['USA', 'Amsterdam', 'Ireland', 'Japan', 'Canada']

print("Original order:") # Basis of the normal order
print(world)

print("\nAlphabetical order:") # Makes it list in Alphabetical order
print(sorted(world))

print("\nOriginal order:") #Shows the order did not change from the original
print(world)

print("\nReverse alphabetical order:") #Makes the list show in a reverse alphabetical order
print(sorted(world, reverse=True))

print("\nOriginal order:") #Shows the order did not change from the original
print(world)

print("\nReversed order:") # Reverses the order of the original code
world.reverse()
print(world)

print("\nOriginal order:") #Shows the order did not change from the original
world.reverse()
print(world)

print("\nAlphabetical order:") # Makes it list in Alphabetical order
world.sort()
print(world)

print("\nReverse alphabetical order:") #Makes the list show in a reverse alphabetical order
world.sort(reverse=True)
print(world)