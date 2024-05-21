try:
    x=2
    print(x)
except NameError:
    print("x nie jest zdefiniowany")
    x = int(input("podaj wartość x: "))
except TypeError as d:
    print(d)
except:
    print("nieokreślony błąd!")
else:
    print(f"opis {x}")
finally:
    y = 90
    print(y)
    print(f"twoje x wynosi: {x}")

print("ciąg dalszy programu")
