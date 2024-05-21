from osoba import Osoba
from pracownik import Pracownik
from student import Student


print("_____________ klasa Osoba _____________")

print("__ osoba 1 ____")
os1 = Osoba("Jan",45,87,173)
print(os1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {os1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {os1.czypracownik()}')

os1.set_kolor_oczu("niebieski")
print(f'nowy kolor: {os1.get_kolor_oczu()}')

print(f'bmi ciała wynosi: {os1.bmi():.2f}, opis: {os1.opisbmi()}')
print(f"zapotrzebowanie energetyczne: {os1.policz_ppm('m'):.2f} kcal")

print("__ osoba 1 ____")
os2 = Osoba("Janina",45,87,173)
print(os2)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {os2.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {os2.czypracownik()}')

os1.set_kolor_oczu("niebieski")
print(f'nowy kolor: {os2.get_kolor_oczu()}')

print(f'bmi ciała wynosi: {os2.bmi():.2f}, opis: {os2.opisbmi()}')
print(f"zapotrzebowanie energetyczne: {os2.policz_ppm('k'):.2f} kcal")

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
print(f'bmi ciała wynosi: {pr2.bmi():.2f}, opis: {pr2.opisbmi()}')
print(f"zapotrzebowanie energetyczne: {pr2.policz_ppm('m'):.2f} kcal")

print("_____________ klasa Student _____________")

print("___ PIERWSZY PRACOWNIK ____")

st1 = Student("Joanna",22,60,170,554535,"Ekonomia",2)
print(st1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {st1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {st1.czypracownik()}')
st1.print_student()

print("___ DRUGI PRACOWNIK ____")

st2 = Student("Tadeusz",44,82,182,78654,"Prawo",4,
              "XYX","radca",12,11300,
              "pływanie",10,"100m - 1min 54s ")
print(st2)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {st2.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {st2.czypracownik()}')
st2.print_student()
print("___ TRZECI PRACOWNIK ____")

st3 = Student("Nadia",25,55,168,75657,"Informatyka",3,
              "Takie IT","programista",2,6700)
print(st3)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {st3.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {st3.czypracownik()}')
st3.print_student()
print("___ CZWARTY PRACOWNIK ____")
st4 = Student("Telimena",21,67,181,656454,"Matematyka",4,
              dyscyplina="pływanie",lataupr=4,bestwynik="100m - 2min 2s ")
print(st4)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {st4.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {st4.czypracownik()}')
st4.print_student()
print(f'bmi ciała wynosi: {st4.bmi():.2f}, opis: {st4.opisbmi()}')
print(f"zapotrzebowanie energetyczne: {st4.policz_ppm('k'):.2f} kcal")
