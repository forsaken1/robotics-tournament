from lib.tasks.task import Task

class First(Task):
    """run by black line"""

    def __init__(self):
        self.passed = False

    def run(self):
        print('Task First runned!')