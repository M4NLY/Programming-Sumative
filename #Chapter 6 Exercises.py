#Chapter 6 Exercises
#1. Pizza Toppings ####################################################
print("Exercise 1: Pizza Toppings")

topping = "\nWhat toppings do you like on your pizza?"    
topping += "\nEnter 'quit' when you are done inputing all of it: "

while True:
    topping = input(topping)
    if topping != 'quit': # If user types quit the code ends
        print(f"  The {topping} is added on the pizza.")
    else:
        break

#2. Movie Tickets ####################################################
print("Exercise 2: Movie Tickets")

age = "How old are you?"
age += "\nEnter 'done' when you are finished. "

while True:
    age = input(age)
    if age == 'done': # This code will finish the code if the user types done
        break
    age = int(age)

    if age < 3: # If the age is lower than 3 
        print(" Toddlers get to watch the movie for free")
    elif age < 13:# If the age is lower than 13
        print("Children who are under 13 years old get to watch the movies for 10$")
    else:
        print("Your ticket is $15") # If not any of the others

#3. Infinity ####################################################
print("Exercise 3: Infinity")

while True:
    print("hello world")
    break #Remove the break statement to stop the infinite loop

#4. Deli ####################################################
print("Exercise 4: Deli")

sandwich_orders = ['Bacon', 'BLT', 'Egg', 'Cheese']
sandwich_done = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.\n")
    sandwich_done.append(current_sandwich)

for sandwich in sandwich_done:
    print(f"I made a {sandwich} sandwich.")

#5. No Pastrami ####################################################
print("Exercise 5: No Pastrami")

sandwich_orders = [
    'pastrami', 'Bacon', 'BLT', 'Egg', 'Cheese']
sandwich_done = []

print("I'm sorry, we're all out of pastrami today.") 
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami') # Removes Pastrami

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.") #Prints all the codes
    sandwich_done.append(current_sandwich)

print("\n")
for sandwich in sandwich_done:
    print(f"I made a {sandwich} sandwich.")