# 
from sys import exit 
from random import randint 
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene 
        current_scene.enter()



class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."   
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothn to blast you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                  Qus you.
                  """))
            return 'death'
            
        elif action == "dodge!":
            print(dedent("""
                  Like a on stomps on your head and eats you.
                  """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                  Lucky 
                  """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              You do 
              """))

        code = f"789"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                  The containe in the right spot.
                  """)) 
            return 'the_bridge'

        else:
            print(dedent("""
                  The lock buzze ship from their ship and you die.
                  """))
            return "death"



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              You burst oto set it off.
              """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                  In a p off.
                  """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                  You phe escape pod to get off this tin can.
                  """))

            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"
class EscapePod(Scene): 

    def enter(self):
        print(dedent("""
              You rush through tou take?
              """))
        
        good_pod = 2#randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                  You jump l ruptures, crushing your body into
                  jam jelly.
                  """))

            return "death"
        else:
            print(dedent(f"""
                  You jumn!
                  """))

            return "finished"

class Finished(Scene):

    def enter(self):
        print("You won! Great job!")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        "finished": Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        print(type(val))
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play() 

