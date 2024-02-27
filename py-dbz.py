# [Edwin Arzu]
# [Sunday Feb 25th, 2024]
# [Python Version : Python 3.11]
# [Fight Club 2.0: The 2nd Rule is...]

################ 1. You need to create a new Python file named utilities.py and place custom functions inside. We will call those functions into this script.

# Import the utilities file 👇
import utilities

################ 2. The fighters need to be moved to a new text file. We will read the code from the file to select fighters.

# Import the fighters.txt file 👇
attacks = utilities.importify('attack.txt')
fighters = utilities.importify('fighters.txt')
utilities.os.system('clear')

##### Announce Game Start #####
print("-" * 50)
print("Welcome to the CELL GAMES! The battle awaits!")
print("-" * 50)
utilities.time.sleep(1)

################ 3. Use the utilities.py to select a fighter from fighters.txt👇###############

# Prompt the user to choose a fighter
while True:
    print("Choose your fighter:")
    print("-" * 50)
    # enumerate()- Python function used to iterate over a sequence such as a list along with an index number
    for i, fighter in enumerate(fighters, 1):
        print(f"{i}. {fighter}")
    pchoice = input("Enter the number corresponding to your fighter: ")
    
    # isdigit()- Returns True if all characters in the string are digits
    if pchoice.isdigit():
        
        # Subtract 1 to convert from 1-indexing to 0-indexing
        fighter_index = int(pchoice) - 1
        
        # len()- Python function that returns the number of items in an object.
        if 0 <= fighter_index < len(fighters):
            player = fighters[fighter_index]
            break
        else:
            print("Invalid fighter choice. Please choose a number between 1 and", len(fighters))
            utilities.time.sleep(2)
            utilities.os.system('clear')
    else:
        print("Invalid input. Please enter a number.")
        utilities.time.sleep(2)
        utilities.os.system('clear')
print("-" * 50)
print("You have chosen:", player)
print("-" * 50)
################ 4. Add a while loop so that the fighters are not the same 👇

# Select a random opponent from the list of fighters
while True:
    opponent = utilities.ranchoice(fighters)
    if opponent != player:
        break
print("Opponent chosen:", opponent)
print("-" * 50)

print(f"{player} has challenged {opponent} in a one on one battle!")
utilities.time.sleep(.8)
print("FIGHT!!!")

################################## Define the attacks ##################################

#####  Attacks List #####
attacks = ['kick' ,'throw' ,'punch']

# I needed to represent what attack beats the other in condition
attack_relations = [
    ('punch' , 'throw'),
    ('throw' , 'kick'),
    ('kick' , 'punch'),
    ('throw' , 'punch'),
    ('kick' , 'throw'),
    ('punch' , 'kick')
]

################################## 5. Exception - Add a while True and exception.

# Hint: the player attack variable should allow the user to pick between the different attack options by pressing 1, 2 or 3 
# Write your code below this row 👇

# Use what you created from Milestone 2 OR Create a loop that will run UNTIL either the player or opponent scores 5 points
# Write your code below this row 👇

##### Initialize Scoring Variables ##### 
pscore = 0
oscore = 0

# Game Loop
while pscore < 5 and oscore <5:
    print(f'Current score   {player}: {pscore}     {opponent}: {oscore} ')
    print("-" * 50)
    utilities.time.sleep(.7)

# 6. Player only - Create an if/elif statement to set the number entry to the correct attack.
# Write your code below this row 👇

# Player chooses an attack
    while True:
        pinput = input("Choose your attack (1 for kick, 2 for throw, 3 for punch): ")
        if pinput.isdigit():
            pattack_index = int(pinput) - 1
            if 0 <= pattack_index < len(attacks):
                pattack = attacks[pattack_index]
                print(f'you have chosen {pattack}')
                break
            else:
                print("Invalid attack choice. Please choose a number between 1 and", len(attacks))
        else:
            print("Invalid input. Please enter a number.")
    
    # 7. Add a while loop so that the attacks are not the same. Use the utilities module.
    # The program randomly picks the attack for the opponent
    while True:
        oattack = utilities.ranchoice(attacks)
        if oattack != pattack:
            break

# Use the scoring system from Milestone 2 
# Write your code below this row 👇
    if pattack == oattack:
        print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')
        utilities.time.sleep(.7)
        print('It\'s a Tie!!')
    else:
        for attack_pair in attack_relations:
            if (pattack, oattack) == attack_pair:
                print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')
                utilities.time.sleep(.7)
                print(f'{player} WINS ROUND!')
                pscore += 1
                break
            elif (oattack, pattack) == attack_pair:
                print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')
                utilities.time.sleep(.7)
                print(f'{opponent} WINS ROUND!')
                oscore += 1
                break
# Once the game is over and someone scored 5 points:
# You may borrow code used for Milestone 2 for this step.
# 8. Print a string that includes the player and opponent names along with the final score to the game.
# Write your code below this row 👇
print("-" * 50)
winner = [f'{player}' if pscore == 5 else f'{opponent}']
print(f'Final score is {pscore} - {oscore} the winner is {winner}.')
# utilities.os.system('clear')
