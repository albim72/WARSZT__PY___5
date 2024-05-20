#przykład 1
def liczby():
    lb = []
    for i in range(16):
        lb.append(i*2+1)
    return lb

def liczby_gen():
    for i in range(16):
        yield i*2+1

print(liczby())
print(liczby_gen())
print(list(liczby_gen()))

for p in liczby_gen():
    print(p)

#przykład 2

def wznowienia(n,k):
    print("wstrzymanie działania...")
    yield 1001
    print("wznowienie działania...")
    yield n+k
    print("działanie - dodawanie. Wstrzymanie")
    print("wznowienie działania...")
    n = 3*n
    yield n - k
    print("działanie - odejmowanie. Wstrzymanie")
    print("wznowienie działania...")
    yield n * k
    print("działanie - mnożenie. Wstrzymanie")
    print("wznowienie działania...")
    yield n / k
    print("działanie - dzielenie. Wstrzymanie")

print(wznowienia(6,7))
print(list(wznowienia(6,7)))

print("_________________________________")

for i in wznowienia(6,8):
    if i == 1001:
        continue
    print(f"yield zwraca wartość: {i}")


