"""
przykład agregacji klas
"""

class Department:
    def __init__(self,nazwa,pracownicy):
        self.nazwa = nazwa
        self.pracownicy = pracownicy

class Pracownik:
    def __init__(self,imie,nazwisko,department):
        self.imie = imie
        self.nazwisko = nazwisko
        self.department = department

dep = Department("Sprzedaż",[])
prac1 = Pracownik("Jan","Kot",dep)
prac2 = Pracownik("Aneta","Kowal",dep)

dep.pracownicy.append(prac1)
dep.pracownicy.append(prac2)

print(dep.pracownicy[0].imie, dep.pracownicy[0].nazwisko)
print(dep.pracownicy[1].imie, dep.pracownicy[1].nazwisko)


