import json

info = '{"organizacja":"Fundacja BIOTECH","miasto":"Zamość","kraj":"Polska"}'
ekstra = {
    "idporjektu":756546,
    "content":"Innowacyjne algorytmy AI oparte na teorii gier",
    "wartość":12_500_000
}

#łącząc oba zasoby (info, ekstra)  zbuduj spójne żródło json i zapisz je w pliku projekt.json

z = json.loads(info)
z.update(ekstra)

newinfo = json.dumps(z,indent=4)

with open("projekt.json","w",encoding="utf-8") as f:
    f.write(newinfo)

with open("projekt.json","r",encoding="utf-8") as f:
    proj_dict = json.load(f)

print(proj_dict)
print(type(proj_dict))
