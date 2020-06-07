"""Main game file"""
from random import choice
from textwrap import dedent
import os
from time import sleep

#Engine
#GameState
#Room
    #StartScreen
    #Bedroom
    #Kitchen
    #Bathroom
    #Corridor
    #Livingroom
#Characters
    #Player
    #Enemy
#Objects
    #Door
    #Key
    #Toaster
#TextFile
#SaveGame
gamestate = {}

class Engine:# use @classmethod so class does not need to be instantiated
    """Contains main game loop and input parser"""

    def clear(self):
        _ = os.system("cls") if os.name == "nt" else os.system("clear")
    ## TODO: implement better parser
    def prompt(self):
        """Prompt for user input and parse into verb, obj1 and obj2"""
        while True:
            command = input(">>> ").lower()
            self.clear()
            try:
                if any(word in command for word in ("with", "and", "on")):
                    verb, obj1, temp, obj2 = command.split(' ')
                else:
                    verb, obj1 = command.split(' ')
                    obj2 = None
            except:
                print("...BEEP, BOP, cannot compute...")
            else:
                return verb, obj1, obj2

# TODO: dedent correctly
    def interact(self, verb, obj1, obj2):
        """call interact function of object"""
        output = ["I don't see any {}",
        "Looking real hard, but no {} in sight.",
        dedent("""\
        I don't have my glasses on,
        but I'm pretty sure there's no {} here.""")]

        if not self.interactable(obj1):
            print(choice(output).format(obj1))
        elif not self.interactable(obj2) and obj2:
            print(choice(output).format(obj2))
        else:
            gamestate.get(obj1).interact(verb, obj2)



    def interactable(self, obj):
        """check if object in player location"""
        bool = False
        if obj in gamestate:
            bool = gamestate.get(obj).location in (player.location, player)
        return bool

    def play(self):
        """Main game loop"""
        while True:
            verb, obj1, obj2 = self.prompt()
            self.interact(verb, obj1, obj2)

class Actor:
    """Parent Actor class. Takes keyword for user input, identifier name, location."""
# check if **kwargs should be used.
# Add argument to define if this actor can activate another (key and lock for example)
    def __init__(self,
                name,
                location=None,
                x_off="A regular {}.",
                examined=False,
                used=False,
                usable=False,
                active=False,
                activates=[],
                takeable=False,
                take_false_text="I can't take that {}.",
                take_true_text=dedent("""\
                *{} added to inventory*
                Maybe I can use that later."""),
                use_words=["use", "open"],
                examine_words=["examine", "inspect"],
                take_words=["take", "get"],
                talk_words=["talk", "scream"]
                ):

        gamestate[name.lower()] = self
        self.name = name
        self.location = location if location else self
        self.x_off = x_off
        self.examined = examined
        self.used = used
        self.usable = usable
        self.active = active
        self.activates = activates
        self.takeable = takeable
        self.takeable_false_text = f"I can't take this {name}."
        self.takeable_true_text = dedent(f"""\
                                        *{name} added to inventory*
                                        Maybe I can use that later.""")
        self.use_words = ["use", "open"]
        self.examine_words = ["examine", "inspect"]
        self.take_words = ["take", "get"]
        self.talk_words = ["talk", "scream"]

        # load command dict with accepted verbs
        self.commands = {}
        self.commands.update({k: self.use for k in self.use_words})
        self.commands.update({k: self.examine for k in self.examine_words})
        self.commands.update({k: self.take for k in self.take_words})
        self.commands.update({k: self.use for k in self.talk_words})

    def interact(self, verb, obj):
        func = self.commands.get(verb)
        if not func:
            print(choice(["I can't do that.", "Nah.", "I don't know how.",
                          "Seems dumb", "No sane person would attempt this."]))
        else:
            return func(obj)

    def take(self, obj):
        if not self.takeable:
            print(self.takeable_false_text.format(self.name))
        else:
            self.location = player
            print(self.takeable_true_text.format(self.name))

    def examine(self, obj):
        print(self.x_off.format(self.name))

    def use(self, obj):
        if not obj:
            print("Using {}".format(self.name))
        if obj in self.activates:
            pass

    def talk(self, obj):
        pass

    def enter():
        pass



class StartScreen(Actor):

    def enter(self):
        player.location = self
        if not self.active:
            print("...")
            sleep(3)
            print("Is this a dream?")
            sleep(2)
            print("I can't see anything.")
            sleep(3)
            print("There, I see some floating words midst this black void!")
            sleep(2)
            print("They read: START, CONTINUE, LOAD, SAVE and EXIT.")
        else:
            print(dedent("""
                         Back in the black void.
                         Only things here are:
                         START, CONTINUE, LOAD, SAVE and EXIT
                         """))

        while True:
            command = input(">>> ").lower()
            if command == "start":
                return start.use()
            elif command in ("save", "load", "continue"):
                print("Not yet implemented.")
            elif command == "exit":
                print("You can run, but you can't hide!")
                exit()
            else:
                print("What? Learn to type properly you dumb fuck!")


class Start(Actor):

    def use(self):
        engine.clear()
        print("Flashy music starts blasting!")
        sleep(2)
        print("A deep resounding voice announces:")
        sleep(2)
        print("WELCOME TO:\n")
        sleep(2)
        print("""
    ___       ____
   /   |     / __ \____ ___  __
  / /| |    / / / / __ `/ / / /
 / ___ |   / /_/ / /_/ / /_/ /
/_/  |_|  /_____/\__,_/\__, /
                      /____/
        """, flush=True)
        sleep(1)
        print("""
\t\t    _          __  __            __    _ ____
\t\t   (_)___     / /_/ /_  ___     / /   (_) __/__
\t\t  / / __ \   / __/ __ \/ _ \   / /   / / /_/ _ \\
\t\t / / / / /  / /_/ / / /  __/  / /___/ / __/  __/
\t\t/_/_/ /_/   \__/_/ /_/\___/  /_____/_/_/  \___/

        """, flush=True)
        sleep(1)
        print("""
\t\t\t\t         ____
\t\t\t\t  ____  / __/
\t\t\t\t / __ \/ /_
\t\t\t\t/ /_/ / __/    _ _ _
\t\t\t\t\____/_/      (_|_|_)

        """, flush=True)
        sleep(2)
        engine.clear()
        print("...ehm...")
        sleep(2)
        player.name = input("...sorry kid, what's your name again?\n")
        sleep(1)
        print("Ah, yeah, alright whatever...")
        sleep(2)
        print("...harrumph...")
        sleep(2)
        engine.clear()
        print("\n\n\n\t\t\tA Day in The Life of {}".format(player.name),
              end=' ', flush=True)
        sleep(2)
        print("the LOSER!")
        sleep(5)
        engine.clear()
        print("BRRRRRRRRRRRRRRIIIIIIIIIIIING\n")
        sleep(2)
        print("BRRRRRRRRRRRRRRIIIIIIIIIIIING\n")
        sleep(2)
        print("BRRRRRRRRRRRRRRIIIIIIIIIIIING\n")
        sleep(2)
        #return bedroom.enter()



class Key(Actor):
    """A Key"""
    def use(self, obj2): # use decorator for checks that are alway the same
        if not obj2:
            print("I need to use this with something.")
        elif obj2 == lock:
            print("You hear a satisfying 'CLICK'.")
        else:
            print("I can't combine those things")



bedroom = Actor("Bedroom", None)
player = Actor("Player", bedroom)
gamestate.update(room=player.location)
key = Key("Key", bedroom)
item = Actor("Item", None)
lock = Actor("Lock", bedroom,
            x_off="Looks like this old lock is a little rusty.")
item2 = Actor("Item2", player)
menu = StartScreen("Menu", None)
start = Start("Start", menu)

engine = Engine()
engine.clear()
#menu.enter()
engine.play()

## TODO: Idea how to store all text and or game logic
## todo: one module for each room
