def dziel(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("Uwaga! dzielenie przez zero!")
    except NameError:
        print("zmienne niezdefiniowane")
    except TypeError as tp:
        print(tp)
    except Exception as ex:
        print(ex)
        print(type(ex))
    else:
        print(f"wynik = {wynik}")
    finally:
        print("policzmy coś jeszcze")

try:
    dziel(5,3)
    dziel(0,5)
    dziel(9,0)
    dziel(0,0)
    dziel(9.343,0.0343)
    dziel(6,True)
    dziel("scssd",56)
    dziel(5)
except TypeError:
    print("Zbyt mała liczba argumentow...")
