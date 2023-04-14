import random

def roll_disc():

    disc_drawing={
        1:(
          "┌───────┐",
          "│   1   │",
          "│   •   │",
          "│       │",
          "└───────┘",
        ),
       2:(
          "┌───────┐",
          "│ •     │",
          "│   2   │",
          "│     • │",
          "└───────┘",
        ),
        3: (
            "┌───────┐",
            "│ • 3   │",
            "│   •   │",
            "│     • │",
            "└───────┘",
        ),
        4: (
            "┌───────┐",
            "│ •   • │",
            "│   4   │",
            "│ •   • │",
            "└───────┘",
        ),
        5: (
            "┌───────┐",
            "│ •   • │",
            "│   5   │",
            "│ •   • │",
            "└───────┘",
        ),
        6: (
            "┌───────┐",
            "│ •   • │",
            "│ • 6 • │",
            "│ •   • │",
            "└───────┘",
        ),
    }
    roll=input("roll the disc?(Yes/No): ")

    while roll.lower()=="yes".lower():
        disc1 = random.randint(1, 6)
        disc2 = random.randint(1, 6)

        print("disc rolled {} and {}".format(disc1,disc2))
        print("\n".join(disc_drawing[disc1]))
        print("\n".join(disc_drawing[disc2]))

        roll=input("Roll afain? (Yes/No):")
roll_disc()