class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)

    

moneem = Shop('moneem')
moneem.add_to_cart('pHone')
moneem.add_to_cart('chips')

print(moneem.cart)