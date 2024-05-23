from dataclasses import dataclass,field

@dataclass
class Fruits:
    names:list = field(default_factory=lambda : [])

fr1 = Fruits()

fr1.names.append("Jabłko")
fr1.names.append("Gruszka")
fr1.names.append("Kiwi")
fr1.names.append("Banan")

print(fr1)

fr2 = Fruits(['Truskawka','Kiwi'])
print(fr2)
