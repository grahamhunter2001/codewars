class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        pos = "q1"
        for cmd in commands:
            if cmd == "0":
                if pos == "q1":
                    pos = "q1"
                elif pos == "q2":
                    pos = "q3"
                elif pos == "q3":
                    pos = "q2"
            elif cmd == "1":
                if pos == "q1":
                    pos = "q2"
                elif pos == "q2":
                    pos = "q2"
                elif pos == "q3":
                    pos = "q2"
        return (pos == "q2")
        
my_automaton = Automaton()
