class Company:
    def __init__(self, name , address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.maneger = []
        self.supervisor = []

class Driver:
    def __init__(self, name ,licence,age) -> None:
        self.name = name
        self.age = age
        
class Counter:
    def __init__(self) -> None:
        pass
    
    def parchais_tiket(self, start, destination):
        pass
    
        
class maneger:
    pass

class Passenger:
    pass