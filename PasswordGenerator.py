#Boiler
import math
import os
import random
os.system('cls')
print ("Password Generator")

#Lists/Variables
adjectives = ["FuNNy", "Cr4zy", "H4ppy", "L0v3ly", "5unny", "K1ll3r", "S1ck", "D4rk", "M4g1c", "Sm4ll", "B1g", "Hug3", "T1ny", "M4551ve", "Cut3", "Ador4bl3", "L0v1ng", "R3D", "Gr33n", "Blu3", "Bl4ck", "Wh1te", "Purpl3", "Yell0w", "C0d3r", "G4M3R"]
nouns = ["Dinosaur@", "Square@", "Cube@", "Rocketship@", "UFO@", "Person@", "Human@", "Apple@", "Rockstar@", "Star@", "Professor@", "Teacher@", "Student@", "Author@", "Artist@"]
number1 = random.randint(1, 999)
specialChars = ["!!", "@@", "##", "$$", "^^", "&&", "**", "--", ";;", ",,", "<<", ">>", "??"]

#Get Random
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = str(number1)
specialChar = random.choice(specialChars)

#Generate Password
pass1 = adjective + noun
pass2 = pass1 + number
password = pass2 + specialChar

#Print Password
print (password)