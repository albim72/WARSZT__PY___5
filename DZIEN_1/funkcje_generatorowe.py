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
