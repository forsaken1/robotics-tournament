from lib.tasks.task import Task
from lib.color import Color
from lib.engine import Engine

class Start(Task):
    """get out from start place"""

    def __init__(self):
        self.passed = False
        self.color = Color()
        self.engine = Engine()

    def run(self):
        if self.color.is_path():
            self.passed = True
        else:
            self.engine.step()
