"""
Description: Mad lib python
Author: Nicolas
"""

# The template for the story

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print ("Mad Libs foi iniciado.")
name = input("Enter a name: ")
adjetivo1 = input("Enter a adjective: ")
adjetivo2 = input("Enter a adjective 2: ")
adjetivo3 = input("Enter a adjective 3: ")

print (name + " " + adjetivo1 + " " + adjetivo2 + " " +  adjetivo3)