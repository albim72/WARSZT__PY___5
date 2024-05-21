from osoba import Osoba
from pracownik import Pracownik

print("_____________ klasa Osoba _____________")
os1 = Osoba("Jan",45,87,173)
print(os1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {os1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {os1.czypracownik()}')

os1.set_kolor_oczu("niebieski")
print(f'nowy kolor: {os1.get_kolor_oczu()}')

print("_____________ klasa Pracownik _____________")

pr1 = Pracownik("Ala",30,56,167,"ABC","dyrektor",5,10900)
print(pr1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {pr1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {pr1.czypracownik()}')
pr1.print_pracownik()
