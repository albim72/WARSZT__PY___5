print("pierwsza linia na dobre otwarcie...")
#komentarz podstawowy
"""
komentarz dokumentacyjny
wieloliniowy
abc
"""

info = """
to nie tylko komentarz
ale wieloliniowy tekst,
który moge wyświetlić
wewnątrz funkcji print...
"""

print(info)
print(info)
print(info)

#CTRL+D - powielanie bloków/linii tesktów
#CTRL +/ - komentowanie/odkomentowanie

#kolekcja - lista

imiona = ["Jan","Piotr","Anna","Nadia","Jan","Tomek","Maria","Anna","Jan"]
print(imiona)
print(imiona[0])
print(imiona[2:4])
print(imiona[1:])
print(imiona[:5])
print(imiona[-1])
print(imiona[-2])

imionaparzyste = imiona[::2]
print(imionaparzyste)
imiona.append("Karol")
print(imiona)
imiona.insert(3,"Leon")
print(imiona)

imiona.remove("Nadia")
print(imiona)
del imiona[5]
print(imiona)

imen = enumerate(imiona,111)
for i,wartosc in imen:
    print(f'index -> {i}, wartość: {wartosc}')

noweimie = imiona
qimie = list(imiona)
pimie = imiona[:]


print(imiona)
print(noweimie)
print(qimie)
print(pimie)

noweimie.append("Kunegunda")

print(imiona)
print(noweimie)
print(qimie)
print(pimie)




