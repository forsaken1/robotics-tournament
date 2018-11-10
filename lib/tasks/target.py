from lib.tasks.task import Task

class Target(Task):
    """final task"""

    def __init__(self):
        self.passed = True

    def run(self):
        pass
