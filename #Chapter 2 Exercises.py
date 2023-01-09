#Chapter 2 Exercises
#1. Variables.####################################################
print("Exercise 1: Variables")
word1 = "I lost my wallet" # This variable holds the phrase "I lost my wallet"
print(word1)

word2 = "I found my wallet" # This variable holds the phrase "I found my wallet"
print(word2)

#2. Variables (Quote)####################################################
print("\nExercise 2: Variables")
print ('Ryan Reynolds once said, "Any kind of crisis can be good. It wakes you up."') # I chose this quote because it is an optimistic quote

#3. Stripping Names####################################################
print("\nExercise 3: Stripping Names")
name = "\tAldric Joaquin C. Manly\n"        

print("Normal text:") #The normal text
print(name)

print("\nUsing lstrip:") #Removes the part of the strip on the left
print(name.lstrip())

print("\nUsing rstrip:") #Removes the part of the strip on the right
print(name.rstrip())

print("\nUsing strip:") #Removes the previous
print(name.strip())

#4. Favorite Number####################################################
print("\nExercise 4: Favorite Number")
num = 8
favnum = (f"My favorite number is {num}.") #Another way to print a code
print(favnum)

#5. USB Shopper####################################################
print("\nExercise 5: USB Shopper")
print("A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.") # The problem of the code
a = 50 // 6 # How much the girl can buy
b = 50 % 6 #How much money she has left
print ("The girl can buy", a , "USB sticks from the store with", b , "euro left.")