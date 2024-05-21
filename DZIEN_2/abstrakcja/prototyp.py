from abc import ABC, abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x
        
    def msg(self):
        print("metoda nieabstrakcyjna klasy abstrakcyjnej")
        
    @abstractmethod
    def policz(self):
        pass
    
    @abstractmethod
    def policz_x(self):
        return 5*self.x
    
