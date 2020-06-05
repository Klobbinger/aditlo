"""Main game file"""
from gamestate import gamestate

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

class Engine:# use @classmethod so class does not need to be instantiated
    """Contains main game loop and player actions"""
    def __init__(self):
        self.stats = {"examine": self.examine,
                      "use": self.use,
                      "take": self.take,
                      "talk to": self.talk
                      }


    def prompt(self):
        """Prompt for user input and translation to appropriate action"""
        while True:
            self.command = input(">>> ").lower()
            try:
                if any((word in self.command for word in ("with", "and"))):
                    verb, obj1, temp, obj2 = self.command.split(' ')
                else:
                    verb, obj1 = self.command.split(' ')
                    obj2 = None

            except:
                print("...BEEP, BOP, cannot compute...")
            else:
                if verb in self.stats:
                    return verb, obj1, obj2
                else: print("I don't know how to do that")
        ## TODO: get words from dict

    def take(self, obj1, obj2):
        """Invoke take() method of object"""
        pass

    def examine(self, obj1, obj2):
        """Invoke examine() method of object"""
        pass

    def talk(self, obj1, obj2):
        """Invoke talk() method of object"""
        pass

    def use(self, obj1, obj2):
        """Invoke use() method of object"""
        #check if operation possible
        if not obj1.stats.get("location") == player.stats.get("location"):
            print(f"I don't see {obj1.stats.get('name')}")
        elif not obj2.stats.get("location") == player.stats.get("location"):
            print(f"I don't see {obj1.get('name')}")
        else:
            return obj1.use(obj2)

    def play(self):
        """Main game loop"""

        while True:
            try:
                verb, obj1, obj2 = self.prompt()
                self.stats.get(verb)(gamestate.get(obj1), gamestate.get(obj2))
            except Exception as e:
                print(e)
                #print("Couldn't find function or object")


class Actor:
    """Parent Actor class. Takes keyword for user input, identifier name, location."""
# check if **kwargs should be used.
# Add argument to define if this actor can activate another (key and lock for example)
    def __init__(self, name, location, **kwargs):
        gamestate[name.lower()] = self
        self.stats = {"name": name,
                      "location": location,
                      "examined": False,
                      "used": False,
                      "usable": False,
                      "active": False,
                      "activates": None
                      }
        self.stats.update(kwargs)

    def take(self):
        print("I can't take the idea of 'Actor'")

    def examine(self):
        pass

    def use(self, obj=None): # use decorator for checks that are alway the same
        if not obj:
            print("Using thing")
        if obj in self.stats.get("activates"):
            pass

    def talk(self):
        pass



class StartScreen(Actor):
    pass



class Key(Actor):
    """A Key"""
    def use(self, obj2=None): # use decorator for checks that are alway the same
        if not obj2:
            print("I need to use this with something.")
        elif obj2 == lock:
            print("You hear a satisfying 'CLICK'.")
        else:
            print("I can't combine those things")



lock = Actor("Lock", "Room1")
key = Key("Key", "Room1")
item = Actor("Item", "Room2")
player = Actor("Player", "Room1")

print(gamestate.items())


engine = Engine()
print(engine.stats)
engine.play()

## TODO: Idea how to store all text and or game logic
