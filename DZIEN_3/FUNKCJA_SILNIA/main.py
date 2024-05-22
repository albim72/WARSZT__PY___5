#silnia -> n!=1*2*3*...*n dla n>=0
#double -> max -> 1.8E+308, min -> 2.4E-324
#n???? przkracza wartość górną double -> n=171

import sys
from liczbaujemna import UjemneN

sys.set_int_max_str_digits(0x10000000)
sys.setrecursionlimit(0x10000000)

def silnia(n):
    if n<0:
        raise UjemneN(n)
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n<0:
        raise UjemneN(n)
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    wynik = silnia(n)
    wynik_rek = silnia_rek(n)
    print(f'silnia od n={n} wynosi {wynik}')
    print(f'silnia rekurencyjna od n={n} wynosi {wynik_rek}')
    print(f'Typ dla wynik: {type(wynik)}')
    print(f'Typ dla wynik_rek: {type(wynik_rek)}')

except UjemneN as un:
    print(un)
except Exception as exc:
    print(exc)
