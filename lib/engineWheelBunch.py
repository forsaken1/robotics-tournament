class EngineWheelBunch:
    def __init__(self, wheels):
        self.wheels = wheels

    def move(self):
        for wheel in self.wheels:
            wheel.move()

    def stop(self):
        for wheel in self.wheels:
            wheel.move()

    def back(self):
        for wheel in self.wheels:
            wheel.back()