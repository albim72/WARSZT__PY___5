from osoba import Osoba
from pracownik import Pracownik
from student import Student


print("_____________ klasa Osoba _____________")
os1 = Osoba("Jan",45,87,173)
print(os1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {os1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {os1.czypracownik()}')

os1.set_kolor_oczu("niebieski")
print(f'nowy kolor: {os1.get_kolor_oczu()}')

print("_____________ klasa Pracownik _____________")

print("___ PIERWSZY PRACOWNIK ____")
pr1 = Pracownik("Ala",30,56,167,"ABC","dyrektor",5,10900)
print(pr1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {pr1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {pr1.czypracownik()}')
pr1.print_pracownik()

print("___ DRUGI PRACOWNIK ____")
pr2 = Pracownik("Robert",50,84,176,"ABC","dyrektor IT",10,
                10100,"Biegi górskie",6,"50km, czas: 6:24:50")
print(pr2)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {pr2.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {pr2.czypracownik()}')
pr2.print_pracownik()

print("_____________ klasa Student _____________")

print("___ PIERWSZY PRACOWNIK ____")

st1 = Student("Joanna",22,60,170,554535,"Ekonomia",2)
print(st1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {st1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {st1.czypracownik()}')
st1.print_student()

print("___ DRUGI PRACOWNIK ____")

print("___ TRZECI PRACOWNIK ____")
