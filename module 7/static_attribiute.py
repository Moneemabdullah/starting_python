class Shopping:
    cart = [] #static attribute
    origin = 'china'
    
    def __init__(self, location,name, ) -> None:
        self.name = name
        self.location = location
        

    
    def purchase(self, item, price, amount):
        ramaining = amount - price
        
    
    