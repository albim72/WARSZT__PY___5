from prototyp import Prototyp

class Regular(Prototyp):
    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return (self.x/self.y)*4

    def policz_x(self):
        return super().policz_x() + self.y*7

    def info(self, msg):
        return f"wiadomość: {msg}"



