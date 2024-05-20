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
