class Phone:
    monufactured = 'chaina'

    def __init__(self,owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price


    def sendSms(self, phone, sms):
        txt = f'sanding {sms} to {phone}'
        print(txt)


MyPhone = Phone('moneem','samsung',19000)
herPhone = Phone('she','iphone',120000)

print(MyPhone.owner,MyPhone.brand,MyPhone.price)
print(herPhone.owner,herPhone.brand,herPhone.price)