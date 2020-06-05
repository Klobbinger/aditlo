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

    def prompt(self):
        """Prompt for user input and translation to appropriate action"""
        self.command = input(">>> ")

    def take(self, obj):
        """Invoke take() method of object"""
        pass

    def examine(self, obj):
        """Invoke examine() method of object"""
        pass

    def talk(self, obj):
        """Invoke talk() method of object"""
        pass

    def use(self,obj):
        """Invoke use() method of object"""

    def play(self):
        """Main game loop"""

        while True:
            self.prompt()
            try:
                if "with" in self.command:
                    func, obj, temp, obj2 = self.command.split(' ')
                    call = gamestate.get(obj).get("identname") + "." + func
                           + "(obj=" + gamestate.get(obj2).get("identname") + ")"
                else:
                    func, obj = self.command.split(' ')
                    obj2 = ""
                    call = gamestate.get(obj).get("identname")+"."+func+"()"
            except:
                print("...beep bop, cannot compute...")

            try:
                exec(call)
            except:
                print("...beep bop, cannot compute...")
            #translator function needed (lexicon)


class Actor:
    """Parent Actor class. Takes keyword for user input, identifier name, location."""
# check if **kwargs should be used.
# Add argument to define if this actor can activate another (key and lock for example)
    def __init__(self, keyword, identname, location, examined=False,
                 usable=False, used=False, usetext=None):
        self.keyword = keyword
        gamestate[keyword] = {"identname": identname,
                              "location": location,
                              "usetext": usetext
                              }

    def take(self):
        print("I can't take the idea of 'Actor'")

    def examine(self):
        pass

    def use(self, obj=None): # use decorator for checks that are alway the same
        if not obj:
            print("Nothing happens")
        elif gamestate.get(obj).get("location") == "Room1": #current player location
            print("I can't combine those things")
        else:
            print(f"I can't find {gamestate.get(obj).get("keyword")}")

    def talk(self):
        pass

    def modify(self, **kwargs):
        for kwarg in kwargs:
            gamestate.get(self.keyword).update(kwargs)



class StartScreen(Actor):
    pass


class Toaster(Actor):
    """A Toaster"""
    def __init__(self, name, location):
        super().__init__(name, location)
        gamestate[location.name][self.name] = {"usable": True}

class Key(Actor):
    """A Key"""
    def use(self, obj=None): # use decorator for checks that are alway the same
        if not obj:
            print("I need to use this with something.")
        elif obj == lock:
            print("You hear a satisfying 'CLICK'.")
            gamestate["lock"]


lock = Actor("Lock", "lock", "Room1")
key = Actor("Key", "key", "Room1")

print(gamestate.get("Actor"))

engine = Engine()
engine.play()

## TODO: Idea how to store all text and or game logic
