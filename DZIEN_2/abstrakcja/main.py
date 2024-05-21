from regular import Regular
from xyz import XYZ

tekst = "ładna pogoda "
print(tekst*8)

rg = Regular(4,5)
print(rg.info("abc 001"))
print(f"policz: {rg.policz()}")
print(f"policz: {rg.policz_x()}")
rg.msg()

xz = XYZ(4,2,7)

print(xz.info("abc 001"))
print(f"policz: {xz.policz()}")
print(f"policz: {xz.policz_x()}")
xz.msg()
