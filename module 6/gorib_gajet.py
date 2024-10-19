class Laptop:
    def __init__(self, brand, price , color, memory) -> None:
        self.brand = brand
        self.price = price
        self.colore = color
        self.momory = memory
        
    def run(self):
        return f'running laptop: {self.brand}'
    
    def coding(self):
        return f'larning python practicing'
    
    
class Phone:
    def __init__(self, brand , price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
        
    def run(self):
        return f'phone tipa tipi kore'
    
    def phone_call(self, number):
        return f'calling to {number}'
    
    
class Camera:
    def __init__(self,brand, price, colore, pixal) -> None:
        self.brand = brand
        self.price  = price
        self.color = colore
        self.pixel = pixal
        
        
    def run(self):
        pass
    
    def  change_lens(self):
        pass
    
    
    
        