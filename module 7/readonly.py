#getter setter read only

class user:
    def __init__(self,name,age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money
        

samsu = user('kopa',21,12000)

print(samsu)