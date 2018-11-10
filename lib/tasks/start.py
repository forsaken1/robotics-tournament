from lib.tasks.task import Task

class Start(Task):
    """get out from start place"""

    def __init__(self):
        self.passed = True

    def run(self):
        print('Task Start runned!')
