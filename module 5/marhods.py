class Phone:
    prize = 20000
    colore = "blue"
    brand = "sumsung"
    feturs = ['camera','FM','display','speker','hammer']

    def call(self):
        print("calling a parson")
        
    def sendSMS(self, phone, sms):
        txt = f'sending {sms} to {phone}'
       # print(txt)
        return txt
        

myPhone = Phone()

myPhone.call()
txt = myPhone.sendSMS('01716133987','hlw baba')

print(txt)