"""
Created on Sun May 5th  2024

@author: Jack Daly
"""




import random as rd
from enum import IntEnum


#The 'fighters' . Their battles will be legendary!
class Fighters(IntEnum): 
    Rock = 0
    Paper = 1
    Scissors =2
    
def players_fighters():
    #Let the player  pick a fighter. 
    players_choice = [f"{fighter.name}[{fighter.value}]" for fighter in Fighters]
    fighters_line= ", ".join(players_choice)
    contender = int(input(f"Choose your fighter!({fighters_line}): "))
    fighter = Fighters(contender)
    return  fighter

def robot_fighters():
    #Let the Dimensional Robots pick a fighter. 
    robot_fighter = rd.randint(0, len(Fighters) - 1)
    robot= Fighters(robot_fighter)
    return robot

def game(players_choice, npc_choice):
    print(f"\nYou choose {players_choice.name}, The Robots choose {npc_choice.name}.\n" )
    #some logic to decide the victor. 
    if players_choice == npc_choice:
        print(f"Both sides selected {npc_choice.name}. It's a tie!")
    elif players_choice == Fighters.Rock:
        if npc_choice == Fighters.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif players_choice==  Fighters.Paper:
        if npc_choice == Fighters.Rock:
            print("Paper covers rock! You win!")
        else: 
            print("Scissors cuts paper! You lose.")
    elif players_choice == Fighters.Scissors:
        if npc_choice == Fighters.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

print("Robots from the 5th dimension have come to challenge you in a battle for Earth!")
while True:
    #Lets run the game!
    try:
        player_choice = players_fighters()
    except ValueError as e:
        range_str = f"[0, {len(Fighters) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    npc_choice = robot_fighters()
    game(player_choice, npc_choice)

    play_again = input("\n The Robots want another round! Play again? (y/n): ")
    if play_again.lower() != "y":
        print("\n The Robots returned home because they were bored.")
        break