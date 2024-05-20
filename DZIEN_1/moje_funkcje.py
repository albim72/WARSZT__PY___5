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
