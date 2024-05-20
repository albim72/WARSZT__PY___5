from funkcje_no2 import gx,rank_list
#przykład 1
n=100
def policz(a:int,b:int,c:float,y:int=109)->int:
    global n
    n = (a+b)**c+y+n
    return n

print(policz(3,5,2,5))
print(policz(5,3.245,90,1.332))
print(policz(2,4,2))

print(n)

#przyklad 2

def zamki(zamek1,zamek2="Czorsztyn",zamek3="Niedzica"):
    return f'ranking zamków: 1 -> zamek {zamek1}, 2 -> zamek {zamek2}, 3 -> zamek {zamek3}'

print(zamki("Malbork","Janowiec","Czersk"))
print(zamki(("Malbork")))

#przykład 3
print(f'wynik 1 -> gx = {gx(4,3,56,3)}')
print(f'wynik 1 -> gx = {gx(4)}')
print(f'wynik 1 -> gx = {gx(4,7)}')
print(f'wynik 1 -> gx = {gx(2.2,k=9)}')
print(f'wynik 1 -> gx = {gx(2.2,k=9,b=2)}')

# przykład 4
rank_list("Java","Python","C#","PHP",nrrank=456)
