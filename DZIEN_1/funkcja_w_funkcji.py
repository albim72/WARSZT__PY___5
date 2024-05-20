#przykład 1 - funkcja wyższego rzędu
def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def konkurs(imie,miejsce,punkty):
    return f'uczestnik konkursu: {imie}, miejsce: {miejsce}, liczba punktów: {punkty}'

def bonus(punkty):
    if punkty>50:
        bn = punkty + 10
    else:
        bn = punkty
    return f'liczba punktów z bonusem: {punkty}'

def osoba(funkcja,*args):
    return funkcja(*args)

def multiosoba(*args):
    bonus(args[1])
    konkurs(*args)
    return "opublikowne wyniki konkursu!"

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Leon","Kraków",56))

print(multiosoba("Anna",19,88))

#przykład 2

def rejestracja(oplata):
    def lista(nrstartowy):
        return f"Twój numer startowy: {nrstartowy}"

    def brak():
        return "Brak wpłaty. Wpłać w ciągu dwóch tygodni!"

    def error():
        return "błąd wpłaty -> 0 - brak, 1 - wpłata"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)(543))
print(rejestracja(0)())
print(rejestracja(-11)())

#przykład 3   funkcje anonimowe

print((lambda f:f*2-3)(6))

b = lambda u,w: u+101-w
print(b(9,4))

def multi(n):
    return lambda a:a*n

print(multi(5)(8))

#przykład 3
liczby = [45,2,5,256,34,222,42,-345,-23,56,789,34,43]

liczby_parz = list(filter(lambda x:x%2==0,liczby))
print(liczby_parz)

cube = list(map(lambda x:x**3,liczby))
print(cube)

def filtruj(dane,test):
    plus = []
    for element in dane:
        if(test(element)):
            plus.append(element)
    return plus

def ekstra_liczba(n):
    return n>=100

print(filtruj(liczby,ekstra_liczba))
