class Oprawa:
    def __init__(self,rodzaj,grubosc):
        self.rodzaj=rodzaj
        self.grubosc=grubosc

    def getoprawa(self):
        return self.rodzaj

class Book:

    op1 = Oprawa("twarda",3.2)
    op = op1.getoprawa()
    def __new__(cls, *args, **kwargs):
        return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30,oprawa=op):
        self.idbook = id
        self.tytul=tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = oprawa
        self.create_book()

    def __repr__(self):
        return f'Książka /{self.idbook}/ {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}'

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

    @property
    def tytul(self):
        return self._tytul

    @tytul.setter
    def tytul(self,nowytytul):
        self._tytul = nowytytul
        self.idbook = 77

class Opis:

    def __init__(blabla,nr_msg,h,info):
        blabla.nr_msg = nr_msg
        blabla.h = h
        blabla.info = info

    def mesage(blabla):
        return f"wiadmość nr {blabla.nr_msg} [{blabla.h}] -> {blabla.info}"


print("____________ wiadomość __________")
opis = Opis(535,"zawiadomienie","Ze względu na remont od godziny 17.00 zostanie odłączony prąd!")
print(opis.mesage())


bk = Book(45,"Wiedźmin","Andrzej Sapkowski",42)
# print(f'do zapłaty: {bk.getcena() - bk.rabat(23):.2f} zł')
print(f'do zapłaty: {bk(23):.2f} zł')
print("zmiana ceny")
bk.setcena(45.6)
# print(f'do zapłaty - po zmianie ceny: {bk.getcena() - bk.rabat(23):.2f} zł')
print(f'do zapłaty - po zmianie ceny: {bk(23):.2f} zł')
print(bk)

bk2 = Book(65,"Hobbit","J.R.R. Tolkien",43,"miękka")
print(bk2)
bk2.tytul = "Hobbit czyli tam i z powrotem"
print(bk2)
print(bk2.tytul)
