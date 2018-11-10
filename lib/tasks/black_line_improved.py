from lib.tasks.black_line import BlackLine

class BlackLineImproved(BlackLine):
    """improved algo with line detectors"""

    def __init__(self):
        super()

    def find_path(self):
        if self.color.right_black():
            self.engine.step_right()
        elif self.color.left_black():
            self.engine.step_left()
        else:
            self.engine.step()
