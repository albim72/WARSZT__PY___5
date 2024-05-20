class Book:
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul=tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def create_book(self):
        print(f"utworzono książkę na podstawie Book...")

    def rabat(self,procent):
        return (procent/100)*self.cena


bk = Book(45,"Wiedźmin","Andrzej Sapkowski",42)
print(f'do zapłaty: {bk.cena - bk.rabat(23)} zł')
