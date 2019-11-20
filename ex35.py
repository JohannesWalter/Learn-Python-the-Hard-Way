# Exercise 35
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = float(choice)
    else:
        dead("Man, learn how to type a number")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""There is a bear here.\n
    The bear has a bunch of honey.\n
    The fat bear is in front of another door.\n
    How are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear kills you")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can g through the door now")
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def elephant_room():
    print("You enter a room and you are awestruck by the sight of a majestic, grey elephant")
    print("You can jump on it or you can walk around it")
    print("What do you choose?")

    choice = input("> ")

    if "jump" in choice:
        print("You jumped on the elephant!")
        exit(0)
    elif "walk" in choice:
        print("A sound choice!")
        exit(0)
    else:
        print("Boohoo")


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and your left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve")


start()