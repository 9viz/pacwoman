
from random import randint

error_insults = [
        "I have been called worse",
        "Oh man. We almost had it. It's gone now!",
        "What is this? Amateur hour?",
        "I... I don't think you did your research",
        "Type in English... I don't understand the gibberish you typed",
        "..... and this is the best you can do?",
        "This is not Windows",
        "Come on, you can do it!",
        "Do u spek inglish?"
        ]

def print_insult():
    num_insults = len(error_insults) - 1
    random_insult_index = randint(0, num_insults)
    insult = error_insults[random_insult_index]
    print(insult)
