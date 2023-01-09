#Chapter 7 Exercises
#1. Message ####################################################
print("Exercise 1: Message")

def display_message():
    message = "I'm learning how to code"
    print(message) # Used to print

display_message()

#2. Favorite Book ####################################################
print("Exercise 2: Favorite Book")
def favorite_book(title): # Def of the book
    print(f"{title} is one of my favorite books.")

favorite_book('Goodbye Eri') # Variable

#3. T-Shirt ####################################################
print("Exercise 3: T-Shirt")

def make_shirt(size, message):
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('XL', 'Shounen brave') # Variables
make_shirt(message="Tomei Answer", size='XXL')

#4. Large Shirts ####################################################
print("Exercise 4: Large Shirts")

def make_shirt(size='large', message='Fight Song'): #The variables
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Outer Science') 

#5. Cities ####################################################
print("Exercise 5: Cities")

def describe_city(city, country='Canada'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Ottowa') #The Cities and countries
describe_city('Tokyo', 'Japan')
describe_city('Toronto')