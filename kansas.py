from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Homeon the Range"

def randomfunfact():
    funfacts = [
        "Kansas is flat.",
        "Witchita is the lasgest city.",
        "Lots of Wizard of Oz references.",
        "Most of Kansas City is in Missouri"
    ]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()