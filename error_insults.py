
from random import randint

error_insults = [
        "I have been called worse",
        "Oh man. We almost had it. It's gone now!",
        "What is this? Amateur hour?",
        "I... I don't think you did your research",
        "Type in English... I can't comprehend the gibberish you typed",
        "..... is this the best you could do?",
        "I'm sorry, this isn't Windows.",
        "Come on, you can do it!",
        "do u spek ingrish?",
        "Ever taken an IQ test?",
        "My kids do better than this!",
        "You're in the wrong class. Primary school's that way.",
        "Let me show you this magical thing called Google...",
        "Get out. I don't care.",
        "I thought we learned how to ask back in kindergarten?",
        "If I own a company, I'd hire you as a beta tester, since you make so many mistakes."
        ]

def print_insult():
    num_insults = len(error_insults) - 1
    random_insult_index = randint(0, num_insults)
    insult = error_insults[random_insult_index]
    print(insult)
