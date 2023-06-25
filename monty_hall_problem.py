'''
Simulating the Hall Problem

In this problem, you have three doors. Two doors contain a goat and one contains the reward.
You pick a door, then the host will remove one of the doors you didn't pick. So there are 
only two doors remaining. The one you picked and the one you didn't pick. The host asks you
if you would like to switch doors, or if you'd like to stick with your door. Should you 
switch doors or should you stick with your first choice? Is there a difference? Let's find
out!
'''
import numpy as np
import random


def NoSwitchDoors(N):
    # Set up doors, assign winner, choose door
    doors = [0,1,2]
    winner = random.randint(0,2)
    chosen_door = random.randint(0,2)

    # Host removes one of the doors you didn't choose
    doors.remove(chosen_door)
    if not (chosen_door == winner):
        removed_door = random.choice(doors)
        doors.remove(removed_door)
    
    # Check if you won or lost
    if chosen_door == winner:
        return 1
    else:
        return 0


def SwitchDoors(N):
    # Set up doors, assign winner, choose door
    doors = [0,1,2]
    winner = random.randint(0,2)
    chosen_door = random.randint(0,2)

    # Host removes one of the doors you didn't choose and switch choice
    doors.remove(chosen_door)
    if not (chosen_door == winner):
        removed_door = random.choice(doors)
        doors.remove(removed_door)
        chosen_door = doors[0]
    
    # Check if you won or lost
    if chosen_door == winner:
        return 1
    else:
        return 0


def main():
    # Set number of simulations 
    N = 100_000

    # Count the number of wins in each case
    num_wins_switch = 0
    num_wins_no_switch = 0
    for i in range(N):
        num_wins_no_switch += NoSwitchDoors(N)
        num_wins_switch += SwitchDoors(N)
        
    # Save the output
    with open("output.txt", "w") as f:
        f.write(f"Number of simulations: N = {N}\n")
        f.write(f"Probability of winning when not switching: {num_wins_no_switch/N * 100}%\n")
        f.write(f"Probability of winning when switching: {num_wins_switch/N * 100}%")


if __name__ == "__main__":
    main()