class Amenity:
    def __init__(self, is_running):
        self.is_running = is_running

    def set_is_running(self, currently_running):
        self.is_running = currently_running
        print(f"{self} is running: {self.is_running}")


class Gas(Amenity):  # In this line we have specified that the class we created
    # called Gas is under the class Amenity previously created
    def __init__(self, is_running, cubic_feet):
        self.cubic_feet = cubic_feet
        super().__init__(is_running)  # This line allows us to inherit properties from the Amenity Class

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.cubic_feet}/cubic ft of gas"


class Electricity(Amenity):
    def __init__(self, is_running, watts):
        self.watts = watts
        super().__init__(is_running)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.watts}/watts of electricity>"


class Water(Amenity):
    def __init__(self, is_running, gallons):
        self.gallons = gallons
        super().__init__(is_running)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.gallons}/gallons of water>"


g = Gas(False, 250)
e = Electricity(False, 104.2)
w = Water(True, 16)

g.set_is_running(True)
g.set_is_running(False)

e.set_is_running(True)
e.set_is_running(False)

w.set_is_running(True)
w.set_is_running(False)