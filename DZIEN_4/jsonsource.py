import json

jsonsource = '{"imię":"Jan","nazwisko":"Kot","wiek":40,"miasto":"Lublin"}'
print(jsonsource)
print(type(jsonsource))

osoba = json.loads(jsonsource)
print(osoba)
print(type(osoba))
print(osoba["miasto"])

samochod = {
    "marka":"Jeep",
    "model":"Compas",
    "rocznik":2020,
    "poj":[2.2,3.2,4.8]
}

print(samochod)

jsonauto = json.dumps(samochod,indent=4)
print(jsonauto)

with open("samochod.json","w",encoding="utf-8") as f:
    f.write(jsonauto)
