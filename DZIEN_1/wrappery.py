import functools

print("przykład dekoratora oraz użycia na wybranych funkcjach...")

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Wywołanie funkcji {func.__name__} z argumentami {args} i kluczowymi argumentami {kwargs}")
        result = func(*args,**kwargs)
        print(f"Funkcja {func.__name__} zwraca {result}")
        return result
    return wrapper

#przykład użycia dekoratora

@log_calls
def add(a,b):
    return a+b

@log_calls
def greet(name,greeting="Witaj"):
    return f"{greeting}! {name}"

#wywołanie udekorowanych funkcji
ra = add(2,5)
print(ra)

gr = greet("Leon")
print(gr)

gr2 = greet("Anna","Cześć")
print(gr2)
