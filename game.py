"""Main game file"""
from random import choice
from textwrap import dedent
from collections import defaultdict
import os
from time import sleep
from sys import argv

script, START_ROOM = argv

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
gamestate = defaultdict(list)

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
                print("*try to properly verbalize what you want to do*")
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

        _obj1 = self.interactable(obj1)
        _obj2 = self.interactable(obj2)
        if not _obj1:
            print(choice(output).format(obj1))
        elif obj2 and not _obj2:
            print(choice(output).format(obj2))
        else:
            _obj1.interact(verb, _obj2)


    def interactable(self, obj):
        """returns interactable object in player location, else None"""

        if gamestate.get(obj):
            for o in gamestate.get(obj):
                if o.location in (player.location, player) and o.visible:
                    return o
        else:
            return False


    def play(self):
        """Main game loop"""
        gamestate.get(START_ROOM)[0].enter()
        while True:
            verb, obj1, obj2 = self.prompt()
            self.interact(verb, obj1, obj2)

class Actor:
    """
    Parent Actor class. Takes keyword for user input, identifier name, location.
    """

    def __init__(self,
                # accepted names
                name=("DUMMY",),
                location=None,
                description=None, # decapitalized and include article
                visible=True,
                # examine
                examined=False,
                examined_false_text=None,
                examined_true_text=None,
                examine_makes_visible=(),
                # use
                used=False,
                used_true_text=None,
                usable=False,
                usable_true_text=None,
                usable_false_text=None,
                usable_with=False,
                del_after_use=False,
                active=True,
                active_true_text=None,
                active_false_text=None,
                activates=(),
                makes_usable=(),
                makes_takeable=(),
                use_makes_visible=(),
                has_special=False,
                # take
                takeable=False,
                takeable_false_text=None,
                takeable_true_text=None,

                entering_text="You entered {}.",
                # accepted commands
                use_words=(),
                examine_words=(),
                take_words=(),
                talk_words=(),
                ):


        self.name = name
        self.description = description or self.name[0]
        self.location = location or self
        self.examined_true_text= (examining_text_true or
                                 self.description)
        self.examined_false_text= (examining_text_false or
                                   self.examined_true_text)
        self.examined = examined
        self.used = used
        self.active = active
        self.activates = activates
        self.takeable = takeable
        self.take_false_text = [take_false_text or
                                f"I can't take this {name[0]}."]
        self.take_true_text = [take_true_text or
                               dedent(f"""\
                               *{name[0]} added to inventory*
                               Maybe I can use that later.""")]
        self.use_words = ("use",) + use_words
        self.examine_words = ("examine", "inspect", "look") + examine_words
        self.take_words = ("take", "get", "pick") + take_words
        self.talk_words = ("talk", "scream") + talk_words
        self.entering_text = entering_text or f"You entered {self.description}"
        self.enters = enters
        self.visible = visible
        self.use_makes_visible = use_makes_visible
        self.examine_makes_visible = examine_makes_visible

        # load gamestate with accepted object names
        for k in self.name:
            gamestate[k.lower()].append(self)

        # load command dict with accepted verbs
        self.commands = {}
        self.commands.update({k: self.use for k in self.use_words})
        self.commands.update({k: self.examine for k in self.examine_words})
        self.commands.update({k: self.take for k in self.take_words})
        self.commands.update({k: self.talk for k in self.talk_words})

        #load inventory
    def inventory_string(self):
        """dervive list of items in room or inventory as text"""

        inventory = []
        for v in gamestate.values():
            for i in v:
                 if (i.location == self and
                     i not in (self, player) and
                     i.visible):
                     inventory.append(i.description)

        # remove duplicates
        inventory = list(dict.fromkeys(inventory))

        inventory[-1] = "and " + inventory[-1]
        string = ', '.join(inventory)
        return string

    def popback(self, list):
        """pop first item and move to back of list"""

        item = list.pop(0)
        list.append(item)
        return item

    def interact(self, verb, obj):
        """check verb and call appropriate method"""

        func = self.commands.get(verb)
        if not obj:
            return func()
        elif obj in self.usable_with and func == self.use:
            return func(obj)
        else:
            print(choice(["I can't do that.",
                          "Nah.", "I don't know how.",
                          "Seems dumb",
                          "No sane person would even attempt to do this."]))

    def take(self):
        """put item in inventory"""

        if not self.takeable:
            print(self.popback(self.takeable_false_text))
        else:
            self.location = player
            print(self.popback(self.takeable_true_text))

    def examine(self):
        """examine object"""
# TODO: examine text if used True and False
        if self.visible:
            if self.examined:
                print(self.popback(self.examining_text_true))
            self.examined = True
            for i in self.examine_makes_visible:
                i.visible = True

        if self.location == self:
            choices = ["Looking around I can see {}.",
                       "I spot {} in my vicinity.",
                       "Alright let's see. We have {} here."]
            print(choice(choices).format(self.inventory_string()))

        if self == player:
            print("I have {} in my pockets.".format(self.inventory_string()))

# TODO: Write decorator for use checks, so it's easier reuseable for custom use functions
    def use(self, obj=None):
        """use object depending on its parameters"""
# TODO: add different "can't interact with specific item" texts
        if not self.active:
            print(self.popback(self.active_false_text))
            return

        elif self.usable_with:

            if not obj:
                print(self.popback(self.active_true_text))
                return

            elif not obj.usable and obj not in self.makes_usable:
                print(self.popback(obj.usable_false_text))
                return

        elif self.has_special:
            return self.special(obj)

        else:
            self.action(obj, internal=True)




            if obj in self.activates:
                obj.active = True
            else:
                for i in self.activates:
                    i.active = not i.activates

            if obj in self.makes_usable:
                obj.usable = True
            else:
                for i in self.makes_usable:
                    i.usable = True

            if obj in self.makes_takeable:
                obj.takeable = True
            else:
                for i in self.makes_takeable:
                    i.takeable = True

            if self.del_after_use:
                self.location = self

            if obj and obj.del_after_use:
                obj.location = obj

    def action(self, obj, internal=False):
        print(self.popback(self.action_text))
# TODO: activate everything in list even if usable with?
        for i in self.use_makes_visible:
            i.visible = not i.visible

        if obj in self.activates:
            obj.active = True
        else:
            for i in self.activates:
                i.active = not i.activates

        if obj in self.makes_usable:
            obj.usable = True
        else:
            for i in self.makes_usable:
                i.usable = True

        if obj in self.makes_takeable:
            obj.takeable = True
        else:
            for i in self.makes_takeable:
                i.takeable = True

        if self.del_after_use:
            self.location = self

        if obj and obj.del_after_use:
            obj.location = obj

    def talk(self):
        choices = ["Ahem...hello?",
                   "So, what's up?",
                   "Ugh, the weather lately! Am I right?",
                   f"Hi, I'm {player.name[0]}"]
        print(choice(choices))

    def enter(self):
        player.location = self
        if not self.active:
            self.active = True
            print(self.entering_text.format(self.description))
        else:
            print(self.entering_text.format(self.description), "Again.")

    def special(self, obj):
        """can be called for special object functions. e.g. a keypad"""

        print("Wow, I'm a special function")
        # if minigame succesfull call action()



class Menu(Actor):

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
            sleep(3)
            print("They read: START, LOAD, SAVE and LEAVE.")
            self.active = True
        else:
# TODO: Move this logic into object being used
            print(self.entering_text)


class Door(Actor):
    """Use to define doors for each direction"""

    def __init__(self, direction=None, leads_to=None, **kwargs):
        super().__init__(**kwargs)
        self.leads_to = leads_to

        self.directions = {"north": ["north", "n", "up"],
                           "east": ["east", "e", "right"],
                           "south": ["south", "s", "down"],
                           "west": ["westh", "w", "left"]}

        for i in direction:
            for k in self.directions[i]:
                gamestate[k.lower()].append(self)

    def use(self, obj):

        if not self.leads_to:
            print("I can't go that way.")
        elif not self.active and self.leads_to:
            print("The door is locked")
        else:
            self.leads_to.enter()


class Start(Actor):

    def use(self, obj):
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
\t\t\t\t\t         ____
\t\t\t\t\t  ____  / __/
\t\t\t\t\t / __ \/ /_
\t\t\t\t\t/ /_/ / __/    _ _ _
\t\t\t\t\t\____/_/      (_|_|_)

        """, flush=True)
        sleep(2)
        engine.clear()
        print("...ehm...")
        sleep(2)
        player.name = input("...sorry kid, what's your name again?\n")
        gamestate[player.name[0]] = player
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
        return bedroom.enter()

class Device(Actor):
    def use(self, obj):
        if player.location != self.enters:
            self.marker = player.location
            print("You're being sucked into the portal!")
            self.enters.enter()
        else:
            print("The portal spits you out!")
            self.marker.enter()


class Load(Actor):
    pass

class Save(Actor):
    pass

class Leave(Actor):
    def use(self, obj):
        print("You can run, but I will haunt you!")
        exit()



class Key(Actor):
    """A Key"""
    def use(self, obj2): # use decorator for checks that are alway the same

        if not obj2:
            print("I need to use this with something.")
        elif obj2 == lock:
            print("You hear a satisfying 'CLICK'.")
        else:
            print("I can't combine those things")



# TODO: get parameters from external file
menu = Menu(name=("Menu","Room", "surroundings"), examining_text_false=dedent("""\
             Nothing but darkness. Any sense of time is absent here.
             """),
             entering_text=dedent("""\
                          Back in the black void.
                          Only things here are:
                          START, LOAD, SAVE, LEAVE.
                          """))

player = Actor(name=("Player","me", "self", "myself"), location=None, use_words=("use", "interact", "touch", "push"))

start = Start(("Start",), location=menu, use_words=("use", "interact", "touch", "push"))
load = Load(("Load",), location=menu, use_words=("use", "interact", "touch", "push"))
save = Save(("Save",), location=menu, use_words=("use", "interact", "touch", "push"))
leave = Leave(("Leave",), location=menu, use_words=("use", "interact", "touch", "push"))

device = Device(("Device",), player, enters=menu, description="a strange device",
                examining_text_false="A strange device without a real shape. A small little bump on the surface does looks movable.")

bedroom = Actor(name=("Bedroom", "Room", "Surroundings"))
key = Key(("Key",), bedroom, description="a brass key")
item = Actor(("Item",), None)
lock = Actor(("Lock",), location=bedroom,
            examining_text_false="Looks like this old lock is a little rusty.",
            description="an old lock")
door = Door(name=("Door",), location=bedroom, direction=("east", "west"), leads_to=menu, use_words=("go", "use", "walk"))
# TODO: fix bug when player name is equal to another object name
# TODO: allow player to only type n to go north. Hard code in parser/interpreter

engine = Engine()
engine.clear()
engine.play()

# TODO: clean up class attributes
## TODO: Idea how to store all text and or game logic
## todo: one module for each room?
