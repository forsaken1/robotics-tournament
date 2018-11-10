# from lib.color import Color
from lib.engine import Engine
from lib.tasks.start import Start
from lib.tasks.first import First

class Tournament:
    def __init__(self):
        self.tasks = [Start(), First()]

    def start(self):
        for task in self.tasks:
            if not task.passed:
                task.run()
