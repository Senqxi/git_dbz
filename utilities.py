import random
import time
import os

# Random Choice
def ranchoice(random_choice):
    return random.choice(random_choice)

# importify
def importify(file_path):
    with open(file_path, "r") as file:
        fighters = file.read().splitlines()
    return fighters
