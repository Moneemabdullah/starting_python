class Bank:
    def __init__(self, balence):
        self.balence = balence
        self.min_withdraw = 100
        self.max_withdraw = 20000

    def chack_balence(self):
        return self.balence

    def deposit(self, amaount):
        if amaount >0:
            self.balence += amaount

    def withdraw(self,amaount):
        if amaount>self.min_withdraw and amaount < self.max_withdraw:
            self.balence -= amaount
        

        
brack = Bank(1022020)

print(brack.chack_balence())


brack.withdraw(12000)

print (brack.chack_balence())