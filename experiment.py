from random import randint
from sys import exit





# ###################################################################################################
# def open():
#     print("You are in!")
#     exit(1)

# def inc():
#     global attempt
#     global mail
#     global pw
#     attempt += 1
#     print(f"You have 10 attempts. Current number of used attempts: {attempt}")
#     if attempt == 9:
#         print("WARNING: this is your last attempt!") 
#     mail = input("Mail? ")
#     pw = input("pw? ")

# def run():
#     global attempt
#     global mail
#     global pw

#     while attempt < 9:

#         if mail == "mail" and pw == "pw":
#             open()
#         elif mail != "mail" and pw == "pw":
#             print("correct pw, but wrong mail")
#             inc()
#         elif mail == "mail" and pw != "pw":
#             print("correct mail, but wrong pw")
#             inc()
#         else:
#             print("both is wrong")
#             inc()

#     if attempt == 9:
#         print("You used all of your attempts")
#         exit(1)


# attempt = 0 
# mail = input("Mail? ")
# pw = input("pw? ")

# run()


####################################################################################################

def message(text):
    print(f"{text}")


def gamble(min, max):
    """Draws a random interger from min to max and prints it"""
    val = randint(min, max)
    print(f"The draw was {val}")

# message("Crazy!!")
# gamble(-5, 5)

class CollectingFunctions(object):
    """Comines the two functions in one class"""

    def __init__(self, text, minn, maxx):
        self.text = text
        self.minn = minn
        self.maxx = maxx

    def message(self):
        text = self.text
        print(f"{text}")


    def gamble(self):
        """Draws a random interger from min to max and prints it"""
        minn = self.minn
        maxx = self.maxx
        val = randint(minn, maxx)
        print(f"The draw was {val}")

a_collecting_functions = CollectingFunctions("WOw, this works!!", -10, 10)
a_collecting_functions.gamble()
a_collecting_functions.message()

####################################################################################################

class Monster(object):
    "Class for all kinds of monsters"

    def description()


