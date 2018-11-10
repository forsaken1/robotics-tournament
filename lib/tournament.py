from lib.tasks.start import Start
from lib.tasks.black_line import BlackLine
from lib.tasks.labyrinth import Labyrinth
from lib.tasks.target import Target
from lib.color import Color
import pyb

class Tournament:
    def __init__(self):
        self.tasks = [Start(), BlackLine(), Labyrinth(), Target()]

    def start(self):
        # self.detect_first_task() # удалит первую задачу, если стартуем сразу на черной линии
        for task in self.tasks:
            while not task.passed:
                task.run()

    def detect_first_task(self):
        measure_count = 0
        color = Color()
        for i in range(10):
            if color.is_path():
                measure_count++
            pyb.delay(100)

        if measure_count > 7:
            self.tasks[1:]
