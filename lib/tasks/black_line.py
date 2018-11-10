from lib.tasks.task import Task
from lib.color import Color
from lib.engine import Engine

class BlackLine(Task):
    """run at black line"""

    def __init__(self):
        self.passed = False
        self.last_rotation = False # False - right, True - left
        self.color = Color()
        self.engine = Engine()

    def run(self):
        if self.color.is_path():
            self.engine.step()
        else:
            self.find_path()

    def find_path(self):
        if self.last_rotation:
            self.engine.step_left()
            # rewrite it after line-detectors adding
            if not self.color.is_path():
                self.engine.step_right()
                self.last_rotation = False
        else:
            self.engine.step_right()
            # rewrite it after line-detectors adding
            if not self.color.is_path():
                self.engine.step_left()
                self.last_rotation = True
