from Animal import *

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self. tetrapod = None
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        print("It's chilly outside, where's the sun at?")

# gekko = Reptile()
# gekko.breathe()