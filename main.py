# This is my first project in Python. It is actually a small, old school text game. The premise is very simple.
# Have fun!

if __name__ == "__main__":
    # There 8 rooms in this game
    # First room where the player spawns
    # Intro Room, Hallways of Bone, Backroom, StairwayToHeaven, Trapdoor Basement, First floor, Altar of Venerations,
    # and the exit chamber. Full diagram in https://cloud.smartdraw.com/editor.aspx?templateId=da34e096-b9cb-4d56-a0ce-d9bdef138714&flags=128#depoId=41004336&credID=-43667867
    rooms = ['introscene', 'HallwaysOfBone', 'Backroom','StairwayToHeaven','AltarsOfVeneration','Trapdoor basement']

    def introScene():
        directions = ["left","right","forward"]
        print("You are now on the torch lit room. You see another division right in front of you, behind a door.\n")
        userInput = ""
        while userInput not in directions:
            print("Options: Ahead - Back")
            userInput = input()
            if userInput == "Ahead":
                HallwaysofBone()
            elif userInput == "back":
                print("Behind you there's only a closed, rusty door. You try to force it open. It won't bulge.")
            else:
                print("Please enter a valid option.")

    # Second room where the player can go. 3 directions: front, back and left.
    def HallwaysofBone():
        directions = ["left","right","forward"]
        print("You are now on the torch lit room. You see another division right in front of you, behind a door.\n")
        userInput = ""
        while userInput not in directions:
            print("Options: Ahead - Back")
            userInput = input()
            if userInput == "Ahead":
                Backroom()
            elif userInput == "back":
                print("Behind you there's only a closed, rusty door. You try to force it open. It won't bulge.")
            else:
                print("Please enter a valid option.")

    # Third room where the player can go. 3 directions: front and back.

    def Backroom():
        directions = ["left","right","forward"]
        print("You are now on the torch lit room. You see another division right in front of you, behind a door.\n")
        userInput = ""
        while userInput not in directions:
            print("Options: Ahead - Back")
            userInput = input()
            if userInput == "Ahead":
                HallwaysofBone()
            elif userInput == "back":
                print("Behind you there's only a closed, rusty door. You try to force it open. It won't bulge.")
            else:
                print("Please enter a valid option.")

    def StairwayToHeaven():
        directions = ["left","right","forward"]
        print("You are now on the torch lit room. You see another division right in front of you, behind a door.\n")
        userInput = ""
        while userInput not in directions:
            print("Options: Ahead - Back")
            userInput = input()
            if userInput == "Ahead":
                HallwaysofBone()
            elif userInput == "back":
                print("Behind you there's only a closed, rusty door. You try to force it open. It won't bulge.")
            else:
                print("Please enter a valid option.")

    while True:
        print("Welcome to the catacombs.\n")
        print("As an intrepid tourist, you stumbled upon a shady looking tunnel in the city of Porto.\n"
              "In the search for the perfect Instagram photo, you follow its path, and ended up losing yourself.\n")
        print("The night has fallen, and darkness reigns in the tunnels which you walk by.\n"
              "You sense a small movement beneath a stone arch right in front of you. You decide you step forward and "
              "investigate.\nIn the arch there is a metallic, rusty door. You open the door.\nIt leads to a small "
              "corridor, illuminated by a couple of torches in each side of the stoned wall.\n\nYou decide to walk in.\n"
              "Shortly after, the door shuts behind you."
              "You must get out of here.\n")
        print("Start by typing your name: ")
        name = input()
        print("Good luck, " +name+ ". Find the way out before you miss your flight.\n\n\n-------------------------"
                                   "----------------------------------------------------------------")
        introScene()



