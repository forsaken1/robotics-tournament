from lib.tasks.start import Start
from lib.tasks.black_line import BlackLine
from lib.tasks.labyrinth import Labyrinth
from lib.tasks.target import Target

class Tournament:
    def __init__(self):
        self.tasks = [Start(), BlackLine(), Labyrinth(), Target()]

    def start(self):
        for task in self.tasks:
            while not task.passed:
                task.run()
