# Abstract sensor class
# Every sensor has it's own position on the car (left-front, left-center...)
class sensor:
    def __init__(self, position: str):
        self.position = position

    def collectData(self):
        self.distance = -1

# This type of sensor represents a camera build into automatic car
# It has it's special field - cameraView - holds camera footage
# It can collectData -> get the camera view,
# and interpreate it (to see if there is something blocking the potentially empty parking space)
class camera(sensor):
    def __init__(self, position: str, cameraView):
        self.position = position
        self.cameraView = cameraView

    def collectData(self):
        self.cameraView = 0
        self.interpretation(self.cameraView)
    def interpretation(self, image):
        # Here in the future will be code that will interpreate the image
        interpreatedAs = 'empty'
        return interpreatedAs

# This type of sensor represents a radar
# It has it's special field - distance -> holds distance from the sensor to the object
# It can collectData -> check how far things are from a car and return this distance
class radar(sensor):
    def __init__(self, position: str, distance: float):
        self.position = position
        self.distance = distance
    def collectData(self, distance: float):
        self.distance = distance
        return distance