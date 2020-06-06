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

## TODO: define __getattr__ to retrieve object attribute from gamestate dict
gamestate = {}

class Engine:# use @classmethod so class does not need to be instantiated
    """Contains main game loop and player actions"""
    def __init__(self):
        self.stats = {"examine": self.examine,
                      "use": self.use,
                      "take": self.take,
                      "talk to": self.talk
                      }

    def clear(self):
        _ = os.system("cls") if os.name == "nt" else os.system("clear")

    def prompt(self):
        """Prompt for user input and translation to appropriate action"""
        while True:
            self.command = input(">>> ").lower()
            self.clear()
            try:
                if any(word in self.command for word in ("with", "and", "on")):
                    verb, obj1, temp, obj2 = self.command.split(' ')
                else:
                    verb, obj1 = self.command.split(' ')
                    obj2 = None

            except:
                print("...BEEP, BOP, cannot compute...")
            else:
                if not verb in self.stats:
                    print("I don't know how to do that")
                elif not gamestate.get(obj1):
                    print(f"I don't see any {obj1} here.")
                elif not gamestate.get(obj2) and obj2:
                    print(f"I don't see any {obj2}")
                else:
                    return verb, obj1, obj2
        ## TODO: get words from dict

    def take(self, obj1, obj2):
        """Invoke take() method of object"""
        if not self.interactable(obj1):
            print(f"I don't see any {obj1.get('name')}")
        else:
            return obj1.take()

    def examine(self, obj1, obj2):
        """Invoke examine() method of object"""
        if not self.interactable(obj1):
            print(f"I don't see any {obj1.get('name')}")
        else:
            return obj1.examine()

    def talk(self, obj1, obj2):
        """Invoke talk() method of object"""
        if not self.interactable(obj1):
            print(f"I don't see any {obj1.get('name')}")
        else:
            return obj1.talk()

    def use(self, obj1, obj2):
        """Invoke use() method of object"""
        if not self.interactable(obj1):
            print(f"I don't see any {obj1.get('name')}")
        elif obj2 and not self.interactable(obj2):
            print(f"I don't see any {obj1.get('name')}")
        else:
            return obj1.use(obj2)

    def interactable(self, obj):
        test = obj.get("location") in (player.get("location"), "player")
        return test

    def play(self):
        """Main game loop"""

        while True:
            verb, obj1, obj2 = self.prompt()
            self.stats.get(verb)(gamestate.get(obj1), gamestate.get(obj2))

                #print("Couldn't find function or object")


class Actor:
    """Parent Actor class. Takes keyword for user input, identifier name, location."""
# check if **kwargs should be used.
# Add argument to define if this actor can activate another (key and lock for example)
    def __init__(self, name, location, **kwargs):
        gamestate[name.lower()] = self
        self.stats = {"name": name,
                      "location": location,
                      "examine": [f"A normal {name}", f"Just a regular {name}"],
                      "examined": False,
                      "used": False,
                      "usable": False,
                      "active": False,
                      "activates": [],
                      "takeable": False,
                      "take_false_text": f"I can't take that {name}.",
                      "take_true_text": dedent(f"""\
                                        *{name} added to inventory*
                                        Maybe I can use that later.""")
                      }
        self.stats.update(kwargs)

    def get(self, key):
        return self.stats.get(key)

    def take(self):
        if not self.stats.get("takeable"):
            print(self.stats.get("take_false_text"))
        else:
            print(self.stats.get("take_true_text"))

    def examine(self):
        print(self.stats.get("examine"))

    def use(self, obj=None): # use decorator for checks that are alway the same
        if not obj:
            print("Using thing")
        if obj in self.stats.get("activates"):
            pass

    def talk(self):
        pass



class StartScreen(Actor):

    def enter(self):
        if not self.stats.get("active"):
            player.stats.update(location=self.get("location"))
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
        print("A DAY", flush=True)
        sleep(1)
        print("  IN THE LIFE", flush=True)
        sleep(1)
        print("    OF ...", flush=True)
        sleep(2)
        engine.clear()
        print("...ehm...")
        sleep(2)
        player.stats.update(name=input(
                            "...sorry kid, what's your name again?\n"))
        sleep(1)
        print("Ah, yeah, alright whatever...")
        sleep(2)
        print("...harrumph...")
        sleep(2)
        engine.clear()
        print("\n\n\n\t\t\tA Day in The Life of {}".format(player.get("name")),
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
        return bedroom.enter()



class Key(Actor):
    """A Key"""
    def use(self, obj2=None): # use decorator for checks that are alway the same
        if not obj2:
            print("I need to use this with something.")
        elif obj2 == lock:
            print("You hear a satisfying 'CLICK'.")
        else:
            print("I can't combine those things")


lock = Actor("Lock", "Room1",
              examine="Looks like this old lock is a little rusty.",
              )

key = Key("Key", "Room1", takeable=True)
item = Actor("Item", "Room2")
player = Actor("Player", "Room1")
start_screen = StartScreen("Menu", "Menu")
start = Start("Start", "Menu")

engine = Engine()
engine.clear()
start_screen.enter()
engine.play()

## TODO: Idea how to store all text and or game logic
## todo: one module for each room
