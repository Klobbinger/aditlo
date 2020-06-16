"""Main game file"""
from random import choice
from textwrap import dedent
from collections import defaultdict
import os
from time import sleep
from sys import argv

from assets import assets

if len(argv) > 1:
    script, START_ROOM = argv
else:
    START_ROOM = "menu"

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
obj_dict = defaultdict(list) # defaultdict so you can append to empty keyvalue
gamestate = {}
WINDOWSIZE_X = 100
WINDOWSIZE_Y = 60
# TODO: implement different shell backgrounds and text colors
# TODO: ensure platform compatibility
class Engine: # use @classmethod so class does not need to be instantiated
    """Contains main game loop and input parser"""

    def clear(self):
        """clear terminal window"""
        _ = os.system("cls") if os.name == "nt" else os.system("clear")
    def gamewindow(self):
        """set terminal window size"""
    # TODO: add linux
        y = os.get_terminal_size().lines
        x = os.get_terminal_size().columns
        if x != WINDOWSIZE_X or y != WINDOWSIZE_Y:
            os.system(f"mode {WINDOWSIZE_X},{WINDOWSIZE_Y}")

    ## TODO: implement better parser
    def prompt(self):
        """Prompt for user input and parse into verb, obj1 and obj2"""
        while True:
            command = input(">>> ").lower()
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
# TODO: check if better to execute direction commands differently
        if obj_dict.get(obj):
            for o in obj_dict.get(obj):
                if o.location in (player.location, player) and o.visible:
                    return o
        else:
            return False


    def play(self):
        """Main game loop"""
        self.gamewindow()
        obj_dict.get(START_ROOM)[0].enter()
        while True:
            self.gamewindow()
            verb, obj1, obj2 = self.prompt()
            self.interact(verb, obj1, obj2)

class Actor:
    """
    Parent Actor class. Takes keyword for user input, identifier name, location.
    """

    def init(self,
        cls=None,
        # accepted names
        name=None,
        location=None, # setting to self makes obj a room
        description=None, # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=None,
        examined_true_text=None,
        examine_makes_visible=(),
        examine_to_activate=False,
        # use
        used=False,
        reusable=False,
        active=False, # can be used
        active_false_text=None, # display if obj is not active
        used_false_text=None, # display first time used
        used_true_text=None, # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=(), # can use usable=False obj and makes usable
        usable_false_text=None, # display if target obj not usable
        usable_with=(),
        usable_with_true_text=None, # display if no target object given
        # action
        use_activates=(),
        makes_takeable=(),
        use_makes_visible=(),
        del_after_use=False,
        has_special=False,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=(),
        leads_to=[],
        in_room_inventory=True,
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=[],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ):

        self.name = name or ["Dummy"]
        self.description = description or self.name[0]
        self.location = gamestate.get(location) or self
        self.visible = visible
        # examine
        self.examined = examined
        self.examined_false_text= examined_false_text or\
            [self.description]
        self.examined_true_text= examined_true_text or\
            self.examined_false_text
        self.examine_makes_visible = examine_makes_visible
        self.examine_to_activate = examine_to_activate
        # use
        self.used = used
        self.reusable = reusable
        self.active = active
        self.active_false_text = active_false_text or ["Nothing happens."]
        self.used_false_text = used_false_text or [f"*used {self.name[0]}*"]
        self.used_true_text = used_true_text or ["I already did that."]
        # use with
        self.usable = usable
        self.makes_usable = [gamestate.get(k) for k in makes_usable]
        self.usable_false_text = usable_false_text or ["That doesn't work yet!"]
        self.usable_with = [gamestate.get(k) for k in usable_with]
        self.usable_with_true_text = usable_with_true_text or\
            [f"I need to use that {self.name[0]} with something else."]
        # action
        self.use_activates = [gamestate.get(k) for k in use_activates]
        self.makes_takeable = [gamestate.get(k) for k in makes_takeable]
        self.use_makes_visible = [gamestate.get(k) for k in use_makes_visible]
        self.del_after_use = del_after_use
        self.has_special = has_special
        #take
        self.takeable = takeable
        self.takeable_false_text = takeable_false_text or\
            [f"I can't take this {self.name[0]}."]
        self.takeable_true_text = takeable_true_text or\
            [dedent(
            f"""\
            *{self.name[0]} added to inventory*
            Maybe I can use that {self.name[0]} later.
            """)]
        # door parameters
        self.direction = direction
        self.leads_to = gamestate.get(leads_to)
        self.in_room_inventory = in_room_inventory
        # room
        self.entering_text = entering_text or [self.description]
        # accepted commands
        self.use_words = (["use"] if not self.direction else
            ["open", "go", "explore"]) + use_words
        self.examine_words = ["examine", "inspect", "look"] + examine_words
        self.take_words = ["take", "get", "pick"] + take_words
        self.talk_words = ["talk", "scream"] + talk_words


        # load command dict with accepted commands
        self.commands = {}
        self.commands.update({k: self.use for k in self.use_words})
        self.commands.update({k: self.examine for k in self.examine_words})
        self.commands.update({k: self.take for k in self.take_words})
        self.commands.update({k: self.talk for k in self.talk_words})

        # load obj_dict with accepted object names
        for k in self.name:
            obj_dict[k.lower()].append(self)

        # load obj_dict with direction synonymes if door/wall
        self.directions = {"north": ["north", "n", "up"],
                           "east": ["east", "e", "right"],
                           "south": ["south", "s", "down"],
                           "west": ["westh", "w", "left"]}

        for i in direction:
            for k in self.directions[i]:
                obj_dict[k.lower()].append(self)

        #load inventory
    def inventory_string(self):
        """dervive list of items in room or inventory as text"""

        inventory = []
        for v in obj_dict.values():
            for i in v:
                if (i.location == self and
                    i not in (self, player) and
                    i.visible and i.in_room_inventory):
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
# TODO: add text based on verb, e.g. "I can't PULL that."
        func = self.commands.get(verb)
        if not obj and func:
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
            if not self.examined:
                print(self.popback(self.examined_false_text))
            print(self.popback(self.takeable_true_text))

    def examine(self):
        """examine object"""
# TODO: examine text if used True and False
        if not self.examined:
            self.examined = True
            for i in self.examine_makes_visible:
                i.visible = True
            if self.examine_to_activate:
                self.active = True
            print(self.popback(self.examined_false_text))

        else:
            print(self.popback(self.examined_true_text))

        if self.location == self:
            engine.clear()
            print(self.description, "\n")
            choices = ["Looking around I can see {}.",
                       "I spot {} in my vicinity.",
                       "Alright let's see. We have {} here."]
            print(choice(choices).format(self.inventory_string()))

        if self == player:
            print("I have {} in my pockets.".format(self.inventory_string()))


    def use(self, obj=None):
        """use object depending on its parameters"""
# TODO: print examine text if not examined before
        if not self.reusable and self.used:
            print(self.popback(self.used_true_text))
            return

        elif not self.active:
            if not self.examined:
                print(self.popback(self.examined_false_text),"\n")
            print(self.popback(self.active_false_text))
            return

        elif self.usable_with:
            if not obj:
                print(self.popback(self.usable_with_true_text))
                return

            elif not obj.usable and obj not in self.makes_usable:
                print(self.popback(self.usable_false_text))
                return

        if self.has_special:
            return self.special(obj)

        else:
            self.action(obj, internal=True)

    def action(self, obj=None, internal=False):
        """action called by own or other object's use method"""
        # TODO: objects can call actions of other objects as well
        if self.used:
            print(self.popback(self.used_true_text))
        else:
            if not self.examined:
                print(self.popback(self.examined_false_text),"\n")
            print(self.popback(self.used_false_text))

        self.used = not self.used

        for i in self.use_makes_visible:
            i.visible = not i.visible

        if obj in self.use_activates:
            obj.active = not obj.active
        else:
            for i in self.use_activates:
                i.active = not i.active

        if obj in self.makes_usable:
            obj.usable = not obj.usable
        else:
            for i in self.makes_usable:
                i.usable = not i.usable

        if obj in self.makes_takeable:
            obj.takeable = not obj.takeable
        else:
            for i in self.makes_takeable:
                i.takeable = not i.takeable

        if self.del_after_use:
            self.location = self

        if obj and obj.del_after_use:
            obj.location = obj

        if self.leads_to:
            self.leads_to.enter()

    def enter(self):
        player.location = self

        engine.clear()
        print(self.name[0], "\n")

        if not self.active:
            self.active = True
            print(self.popback(self.entering_text))

    def special(self, obj):
        """can be called for special object functions. e.g. a keypad"""

        print("Wow, I'm a special function")
        # if minigame succesfull call action()


    def talk(self):
        choices = [
        "Ahem...hello?",
        "So, what's up?",
        "Ugh, the weather lately! Am I right?",
        f"Hi, I'm {player.name[0]}"
        ]

        print(choice(choices))

class Player(Actor):
    def __init__(self):
        globals()["player"] = self

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
            print(self.name[0])

class Start(Actor):

    def special(self, obj=None):
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
        player.name[0] = input("...sorry kid, what's your name again?\n")
        obj_dict[player.name[0]].append(player)
        sleep(1)
        print("Ah, yeah, alright whatever...")
        sleep(2)
        print("...harrumph...")
        sleep(2)
        engine.clear()
        print("\n\n\n\t\t\tA Day in The Life of {}".format(player.name[0]),
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
        self.action()

class Device(Actor):
    def special(self, obj):
        if player.location != self.leads_to:
            self.marker = player.location
            print("You're being sucked into the portal!")
            self.leads_to.enter()
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



if __name__ == '__main__':

    gamestate.update({k: globals().get(v.get("cls"))() for k, v in assets.items()})

    for k, v in gamestate.items():
        v.init(**assets.get(k))


# TODO: fix bug when player name is equal to another object name
# TODO: allow player to only type n to go north. Hard code in parser/interpreter
    engine = Engine()
    engine.clear()
    engine.play()


## TODO: Idea how to store all text and or game logic
