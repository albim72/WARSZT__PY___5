from osoba import Osoba

os1 = Osoba("Jan",45,87,173)
print(os1)
nlat = int(input("podaj liczbę lat: "))
print(f'wiek za {nlat} lat -> {os1.wiek_za_n_lat(nlat)}')
print(f'czy osoba jest pracownikiem: {os1.czypracownik()}')

os1.set_kolor_oczu("niebieski")
print(f'nowy kolor: {os1.get_kolor_oczu()}')
