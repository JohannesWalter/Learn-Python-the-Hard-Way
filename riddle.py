def sphinx():
    print("You encounter a sphinx!")
    print("She has a riddle for you. You have only five attempts to answer the question correctly...")
    for i in range(0,9):
        print(f"You have {10-i} trials left")
        answer = input("> What is 5 + 5 ? ")
        if "10" in answer:
            print("congratulations! you are correct!")
            break
        else:
            print("Try again!")

#sphinx()

inventory = []

def pick_item(item):
    print("This is your current inventory: ")
    print(inventory)
    #choice = input("> Would you like to pick up the " + str(item))
    print("You pick up a " + str(item) +". It is automatically added to your inventory and ready for you in a fight when you need it")
    inventory.append(str(item))
    print("This is your updated inventory: ")
    print(inventory)

pick_item("sword")
pick_item("wand")
pick_item("axe")


# def add(a, b):
#     z = a + b
#     print(z)

# add(2,4)

# def fun(word):
#     print(word)

# fun("hello")