water = 1 #Variables needed for the item's prices
lays = 3
cola = 2
sprite = 2
snickers = 2.5
doritos = 5



print(" ____________________________________________") #text art of a vending machine
print("|///////////////////////////////////////////|")
print("|\|                               |/////////|")
print("|\|  ____                         |/////////|")
print("|\| |    |         ^^^^^^^^       |/////////|")
print("|\| |    |         \      \       |/////////|")
print("|\| |    |          \ chips\      |/////////|")
print("|\| |    |          /      /      |/////////|")
print("|\| ------          \      \      |/////////|")
print("|\|===============================|/////////|")
print("|\|'''''''''''''''''''''''''''''''|/////////|")
print("|\|                               |/////////|")
print("|\|  ____                         |/////////|")
print("|\| |    |             ^^^        |/////////|")
print("|\| |    |             \  \       |/////////|")
print("|\| |    |              \__\      |/////////|")
print("|\| |    |              /__\      |/////////|")
print("|\| ------             ____/      |/////////|")
print("|\|===============================|/////////|")
print("|\|'''''''''''''''''''''''''''''''|/////////|")
print("|\|                               |/////////|")
print("|\|  _H_                          |/////////|")
print("|\| /   \            ^^^^^^^      |/////////|")
print("|\| |    |           \      \     |/////////|")
print("|\| |    |            \      \    |/////////|")
print("|\| |    |            /      /    |/////////|")
print("|\| |____|            \      \    |/////////|")
print("|\|===============================|/////////|")
print("|\|'''''''''''''''''''''''''''''''|/////////|")
print("---------------------------------------------")
print("=====                                  =====")
print("=====                                  =====")
print("=====                                  =====")
print("=====                                  =====")

money = int(input("How much money do you use?")) #Asking the user on how much they will use in the vending machine

Vendingmachine = ['Cola, 001, 2 dhs', 'Water, 002, 1 dhs', 'Sprite, 003, 2 dhs', 'Snickers, 004, 2.5 dhs', 'Lays, 005, 4 dhs', 'Doritos, 006, 5 dhs'] #List of items in the vending machine
for x in Vendingmachine:
    print(x) #Used to make the output of the list of items look a lot cleaner



print("You have ", money," dhs on you") #To show the user how much they have
answer = input("What would you like from the vending machine? :  ") #asks if the user which item they would want

if answer == '001': #If the user types 001 the user will get water

    if water <= money: #If the user has enough money they will buy the item and the code ends
        print("You bought water")
        print("You have ",money - water, "dhs left")

    elif water > money: #If the user does not have enough money they will not be able to buy the item
        print("Insufficient funds")
elif answer == '005': #If the user types 001 the user will get lays chips

    if lays <= money: #If the user has enough money they will buy the item and the code ends
        print("You bought Lays chips")
        print("You have ",money - lays, "dhs left")

    elif lays > money: #If the user does not have enough money they will not be able to buy the item
        print("Insufficient funds")
elif answer == '002': #If the user types 001 the user will get a cola

    if cola <= money: #If the user has enough money they will buy the item and the code ends
        print("You bought Cola")
        print("You have ",money - cola, "dhs left")

    elif cola <= money: #If the user does not have enough money they will not be able to buy the item
        print("Insufficient funds")
elif answer == '003': #If the user types 001 the user will get sprite

    if sprite <= money: #If the user has enough money they will buy the item and the code ends
        print("You bought a Sprite")
        print("You have ",money - sprite, "dhs left")
    
    elif sprite > money: #If the user does not have enough money they will not be able to buy the item
        print("Insufficient funds")
elif answer == '006': #If the user types 001 the user will get a bag of doritos

    if doritos <= money: #If the user has enough money they will buy the item and the code ends
        print("You bought Doritos chips")
        print("You have ",money - doritos, "dhs left")

    elif doritos > money: #If the user does not have enough money they will not be able to buy the item
        print("Insufficient funds")
elif answer == '004': #If the user types 001 the user will get a snickers bar

    if snickers <= money: #If the user has enough money they will buy the item and the code ends
        print("You bought a Snickers bar")
        print("You have ",money - snickers, "dhs left")

    elif snickers > money: #If the user does not have enough money they will not be able to buy the item
        print("Insufficient funds")
else:
    print("Invalid code") #if the user types anything other than what is in the vending machine the output will be "Invalid code"