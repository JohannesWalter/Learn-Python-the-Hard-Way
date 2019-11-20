from random import randint
from time import sleep

hp_dragon = 100
hp_player = 100

def health_status():
    global hp_dragon
    global hp_player
    print(f"You have {hp_player} hp, the dragon now has {hp_dragon} hp.")

def dragon():
    global hp_dragon
    global hp_player
    print("You now fight the dragon!...")
    sleep(2)
    print("The dragon has three different types of attacks. Each is most successfully paraded by a move of yours...")
    while (hp_dragon > 0 and hp_player > 0):
        attack = randint(0,2)
        if attack == 0:
            bite()
            input("> ")
        elif attack == 1:
            hit_w_tail()
            input("> ")
        elif attack ==2:
            spit_fire()
            input("> ")
        else:
            print("Error #1 this is not an attack of the dragon that should be possible")
    print(f"{hp_dragon} and {hp_player}")

def bite():
    global hp_dragon
    global hp_player
    print("The dragon tries to bite you!")
    choice = input("> How do you react? 'leap' backwards or do you 'block' the bite? ")
    if 'leap' in choice:
        print("You leap backwards!")
        effect = randint(0,99)
        if effect < 70:
            print("Successfully! The dragon bites in the air, but you are already safely on the side. You can even stab the dragon and damage him!")
            hp_dragon -= randint(10, 20)
            health_status() 
        else:
            print("You leap backwards, but the dragon reaches you anyway, unlucky you!")
            hp_player -= randint(15,20)
            health_status() 
    elif 'block' in choice:
        print("You try to block the dragon's attack!")
        effect = randint(0,99)
        if effect < 20:
            print("You block successfully! Wow! That is very difficult to achieve! ...You even give him a hit!")
            hp_dragon -= randint(10, 20)
            health_status()
        else:
            print("You want to block the bite, but that's very difficult! You fail this time...The dragon hurts you!")
            hp_player -= randint(20,30)
            health_status()
    else:
        print("You can choose between 'leap' backwards to avoid the bite or you try to 'block' the bite")

def hit_w_tail():
    global hp_dragon
    global hp_player
    print("The dragon tries hit you with his tail!")
    choice = input("> How do you react? 'stab' the tail with your sword or 'jump' on the tail? ")
    if 'stab' in choice:
        print("You try to stab the tail as it flies towards you!")
        effect = randint(0,99)
        if effect > 49:
            print("You stab the tail right in the middle! Dragon blood spills on you as the dragon howls loudly")
            hp_dragon -= randint(10,20)
            health_status()
        else:
            print("You try to stab the tail, but the dragon moves too fast! Instad of stabbing it, he hits you and slamms you against the wall!")
            hp_player -= randint(10,20)
            health_status()
    elif 'jump' in choice:
        print("You try to jump on the tail!")
        effect = randint(0,99)
        if effect > 85:
            print("You jump exactly at the right moment and land the the tail!! The dragon is furious! From there you can bury your sword deep in the beasts flesh!")
            hp_dragon -= randint(30,35)
            health_status()
        else:
            print("You try to jump on the tail, but you slip and miss it...at least you don't get hurt")
            health_status()
    else:
        print("You can 'stab' or 'jump' at this point.")

def spit_fire():
    global hp_dragon
    global hp_player
    print("The dragon spits fire!")
    choice = input("> How do you react? 'run' away or use a 'magic' spell to block it and throw the fire back at the dragon? ")
    if 'run' in choice:
        print("You run away! Smart move, dragon fire burns like hell!")
        print("The dragon looks like he got a little bit weaker through his attack of his")
        hp_dragon -= randint(1,5)
        health_status()
    elif 'magic' in choice:
        print("You use the magic spell!")
        effect = randint(0,99)
        if effect < 20:
            print("A powerful white light shoots out of your wand! You block the fire and it heads back to the dragon, hurting him badly!")
            hp_dragon -= randint(20,25)
            health_status()
        else:
            print("The spell and the fire hit on each other and with a loud 'bang!' both you and the dragon are being thrown backwards!")
            hp_dragon -= 10
            hp_player -= 5
            health_status()
    else:
        print("You can 'run' or use a 'magic' spell at this point.")

#dragon()
#bite()