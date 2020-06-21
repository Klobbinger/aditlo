import sys
from collections import defaultdict
from game import Engine

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)


class ConvoNode:
    """
    Holds attributes and conditions for Text to be displayed in conversation
    """
    def __init__(self, text="text", active=True, reusable=True, npc=False):
        # self.ident = None
        # self.cls = "ConvoNode"
        self.text = text
        # self.current = False
        self.active = active
        self.reusable = reusable
        self.npc = npc
        #self.activates = activates
        # self.min_wit = 0
        # self.min_str = 0
        # self.min_balls = 0

    def ping(self):
        if self.active: # TODO: also test for attribtues etc.
            return True
        else:
            return False

    def say(self):
        if not self.reusable:
            self.active = False
        return self.script()

    def script(self):
        pass

class ConvoEngine:
    """
    interprets conversation graph, ConvoNode attributes, conditions and scripts
    """



engine = Engine()
d = defaultdict(set)
d['0'].add('A')
d['A'].add('B')
d['A'].add('C')
d['B'].add('A')
d['C']

convos = dict(
    A=ConvoNode("Hello", True, True, True),
    B=ConvoNode("Hi", True, False, False),
    C=ConvoNode("Bye", True, True, True)
    )

def convo():
    engine.clear()
    current = d['0']
    while current:
        choices = [node for node in current if convos[node].ping()]
        print(choices)
        if len(choices) > 1:
            for i, node in enumerate(choices, start=1):
                print(" ", i, ". ", convos[node].text, sep='')
            choice = get_choice(choices)
            engine.clear()
        else:
            choice = choices[0]
            print(convos[choice].text, end="\n\n")

        convos[choice].say()
        current = d[choice]

def get_choice(choices):
    while True:
        try:
            return choices[int(input("\n>>> "))-1]
        except:
            print("Choose one of the printed options")

convo()

#test pull
# TODO: https://stackoverflow.com/questions/5290994/remove-and-replace-printed-items
