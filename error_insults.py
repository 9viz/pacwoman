from random import choice 

ERROR_INSULTS = [
# error insults from diamondburned and sudo's header files
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
        "If I own a company, I'd hire you as a beta tester, since you make so many mistakes.",
        "Just what do you think you're doing Dave?",
        "That's something I cannot allow to happen",
        "Take a stress pill and think things over",
        "Sorry about this, I know it's a bit silly",
        "And you call yourself a Rocket Scientist!",
        "Wrong! You cheating scum!",
        "Maybe if you used more than just two fingers...",
        "Listen, brocolli brains, I don't have time to listen to this trash",
        "I've seen penguins that can type better than that",
        "Have a gorilla..."
        ]

def print_insult():
    print(choice(ERROR_INSULTS))
