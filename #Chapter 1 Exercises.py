#Chapter 1 Exercises
#1. Print Strings####################################################
print("Exercise 1: Print String")
print("Hello World\n")  #Used to print "Hello World"

#2. Print the Version of Python####################################################
print("Exercise 2: Print the Version of Python")
from argparse import Namespace
import sys # I imported the sys so I can use the next 2 codes
from typing import List
print (sys.version) #The version of the python
print (sys.version_info) #Information of the version

#3. Print date and Time####################################################
print("\nExercise 3: Print date and Time")
import datetime
now = datetime.datetime.now()
print ("Current date and time: ")
print (now.strftime("%Y-%m-%d, %H:%M:%S"))

#4. Strings Concatination####################################################
print("\nExercise 4: Strings Concatination")
word1 = "There’s only one word in the dictionary that’s spelled wrong."
word2 = " What is it?"
word3 = " The word “wrong.” It’s the only word that’s spelled W-R-O-N-G."
print( word1 + word2 + word3)

#5. Compute area of Circle####################################################
print("\nExercise 5: Compute area of Circle")
r = int(input("Enter radius of circle : "))
answer = (3.14 * r**2)
print ("The area of the circle is:", answer)