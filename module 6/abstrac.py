from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def eat(self):
        print (f'khana khabo')
        
        
        
class Monkey(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def eat(self):
        print(f'nothing to say')
        
        
        
        