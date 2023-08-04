
class Robot():
    def __init__(self, Atificial_intellegent, wheels, sensor):
        self.Atificial_intellegent = Atificial_intellegent
        self.wheels = wheels
        self.sensor = sensor

class Robot_vacuum(Robot):
    def __init__(self, Atificial_intellegent, wheels, sensor, vacuum):
        super().__init__(Atificial_intellegent, wheels, sensor)
        self.vacuum = vacuum
        
    def sucking(self):
        return f"this robot has {self.Atificial_intellegent} AI, {self.wheels} wheels, {self.sensor} sensor, and {self.vacuum}"
    
class Robot_food_servant(Robot):
    def __init__(self, Atificial_intellegent, wheels, sensor, disk_holder, communication):
        super().__init__(Atificial_intellegent, wheels, sensor)
        self.disk_holder = disk_holder
        self.communication = communication
    
    def serving(self):
        return f"this robot has {self.Atificial_intellegent} AI, {self.wheels} wheels, {self.sensor} sensor, {self.disk_holder} disk holder and {self.communication} communication"
    
class Robot_security(Robot):
    def __init__(self, Atificial_intellegent, wheels, sensor, knight_stick, siren, jet):
        super().__init__(Atificial_intellegent, wheels, sensor)
        self.knight_stick = knight_stick
        self.siren = siren
        self.jet = jet

    def on_guard(self):
        return f"this robot has {self.Atificial_intellegent} AI, {self.wheels} wheels, {self.jet}, {self.sensor} sensor, {self.knight_stick}, {self.siren} siren, {self.jet} jets"


vacuum = Robot_vacuum("Josephia", 4, "dust", 2)
food_sevant = Robot_food_servant("Hummaner", 2, "visual", 2, "good")
guard = Robot_security("Micheal", "no", "night vision", 1, 1, 2)

print(vacuum.sucking())
print(food_sevant.serving())
print(guard.on_guard())