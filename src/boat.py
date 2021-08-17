class Boat:
    def __init__(self, name, top_speed):
        self.name = name
        self.top_speed = top_speed

    def launch(self):
        return "Ship Ahoy!"

class Speedboat(Boat): 
    def __init__(self, name, top_speed, engine_size):
        super().__init__(name, top_speed)
        self.engine_size = engine_size

    def launch(self):
        return f"Ship Ahoy! Vrroooomm!"

class Yacht(Boat):
    def __init__(self, name, top_speed, sail_size):
        super().__init__(name, top_speed)
        self.sail_size = sail_size

speedboat = Speedboat("The Artful Dodger", 45, 32)
print(speedboat.launch())
print(speedboat.engine_size)

yacht = Yacht("The Jolly Rancher", 28, "Large")
print(yacht.launch())
print(yacht.sail_size)