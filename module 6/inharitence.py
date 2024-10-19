# commom fantionality class
# base class

# dericed class 


class Device:
    def __init__(self, brand, price,color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'running laptop: {self.brand}'
    

class Laptop:
    def __init__(self, ssd, memory) -> None:
        self.momory = memory
        self.ssd = ssd
    
    def coding(self):
        return f'larning python practicing'
    
    
class Phone:
    def __init__(self, brand , price, color, dual_sim) -> None:
        self.dual_sim = dual_sim
        
    def phone_call(self, number):
        return f'calling to {number}'
    
    
class Camera:
    def __init__(self,brand, price, colore, pixal) -> None:
        self.pixel = pixal
        
    
    def  change_lens(self):
        pass
    
    
#inbharitence

my_phone = Phone(True)
        