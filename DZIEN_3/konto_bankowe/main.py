from konto import KontoBankowe

konto1 = KontoBankowe("1234567890", "Jan Kowalski", 1000.0)
print(konto1.sprawdz_saldo())  # Powinno zwrócić 1000.0
konto1.wplata(500.0)
print(konto1.sprawdz_saldo())  # Powinno zwrócić 1500.0
konto1.wyplata(200.0)
print(konto1.sprawdz_saldo())  # Powinno zwrócić 1300.0
konto1.wyplata(1500.0)         # Powinno wyświetlić komunikat o braku wystarczających środków
print(konto1.sprawdz_saldo())  # Powinno zwrócić 1300.0
