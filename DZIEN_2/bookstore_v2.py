class Book:
    def __new__(cls, *args, **kwargs):
        return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul=tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return f'Książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}'

    def __call__(self,proc):
        return self.getcena() - self.rabat(proc)

    def create_book(self):
        print(f"utworzono książkę na podstawie Book...")

    def rabat(self,procent):
        return (procent/100)*self.cena

    def costam(self):
        return "coś tam!"

    def getcena(self):
        return self.cena

    def setcena(self,nowacena):
        self.cena = nowacena


bk = Book(45,"Wiedźmin","Andrzej Sapkowski",42)
# print(f'do zapłaty: {bk.getcena() - bk.rabat(23):.2f} zł')
print(f'do zapłaty: {bk(23):.2f} zł')
print("zmiana ceny")
bk.setcena(45.6)
# print(f'do zapłaty - po zmianie ceny: {bk.getcena() - bk.rabat(23):.2f} zł')
print(f'do zapłaty - po zmianie ceny: {bk(23):.2f} zł')
print(bk)
