from operacje import calculate
from switch import Switch,case

print("____ użycie instrunkcji match-case ________")
calculate('+',5,6)
calculate('-',7,6)
calculate('*',2,11)
calculate('/',5,3)
calculate('/',5,0)
calculate('?',52,6)

print("_____ użycie narzędzi Switch - case ______")

n = int(input("podaj cyfrę systemu dzisiętnego (0-9): "))
while Switch(n):
    if case(0):
        print("n jest równe 0")
        break
    if case(1,4,9):
        print(f"n jest kwadratem innej liczby")
        break
    if case(2):
        print(f"n jest liczbą parzystą")
    if case(2,3,5,7):
        print(f"n jest liczbą pierwszą")
        break
    if case(6,8):
        print(f"n jest krotnością liczby 2")
        break
    print("pisz tylko cyfry")
    break
