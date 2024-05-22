class Obliczenia:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def moblicz(x,y,z):
        return (x+y)*z
    
Obliczenia.moblicz = staticmethod(Obliczenia.moblicz)
