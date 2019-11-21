from sys import exit
from random import randint
from time import sleep
import monster

def lobby():
    print("You are in the ZEW lobby. It is night and the room is only dimly light by the greyish moonlight")
    print("You can go 'left' up some stairs or 'right' up some stairs")

    choice = input("> ")

    if "left" in choice:
        stairs2()
    elif "right" in choice:
        stairs1()
    else:
        print("Type 'left' or 'right', dumbo")

def stairs1():
    print("You walked up some stairs...")
    print("Now you can choose between turning 'left' up some more stairs. Or 'right' into the rooms 1 2 3. Or 'back' into the lobby")

    choice = input("> ")

    if "left" in choice:
        pass
        #up1()
    elif "right" in choice:
        room123()
    elif "back" in choice:
        lobby()
    else:
        print("unknown command")

def stairs2():
    print("You are in a stairway plateau")
    print("Now you can choose between turning 'up' up some more stairs. Or 'left' into the 'Europe' rooms. Or 'back' into the lobby")

    choice = input("> ")

    if "left" in choice:
        europe()
    elif "up" in choice:
        pass
        #up2()
    elif "back" in choice:
        lobby()
    else:
        print("unknown command")

def room123():
    print("You are in the hallway leading to rooms 1, 2 and 3. It is still dark. At the end of the hallway, close to room 3, you see a shimmering light. Do you 'approach' it, do you 'yell hello?' or do you go 'back' to the stairs 1?")

    choice = input("> ")
    if "approach" in choice:
        fight()
    elif "yell" in choice:
        response()
    elif "back" in choice:
        stairs1()
    else:
        print("unknown command")

def fight():
    print("You slowly approach the light...")
    sleep(2)
    monster.dragon()
    print("GAME OVER")
    exit(0)

def response():
    print("You yell: Who is there?")
    print("As an answer, you hear a ghost howling!")
    print("You say: Get lost bitch!")
    print("Congratulations, you beat the ZEW ghost, you win!")
    print("The End")
    exit(0)

def europe():
    print("Nothing special seems to happen here")
    print("You turn back")
    stairs2()

def fight_ghost():
    hp_ghost = 100
    hp_player = 100
    print("You can either 'hit' the ghost or you try to 'shoo' it away...You and the ghost both have 100 health points btw")
    choice = input("> ")
    if "hit" in choice:
        print("You chose to hit the ghost!")
        sleep(1)
        print("The ghost stumbles...")
        player_hit = randint(0,20)
        hp_ghost -= player_hit
        print(f"Your hit caused {player_hit} damage points! The ghost has now {hp_ghost} health points left")
        print("Now the ghost attacks you!")
        ghost_hit = randint(0,18)
        hp_player -= ghost_hit
        sleep(1)
        print(f"Autsch! The ghost caused you to lose {ghost_hit} health points. You now have {hp_player} health points left")
    elif "shoo" in choice:
        pass
    else:
        print("You can choose between 'hit' and 'shoo'")

lobby()