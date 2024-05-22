from dataclasses import dataclass,astuple,asdict,field

@dataclass
class City:
    city:str
    woj:str
    stolica:bool


@dataclass
class Person(City):
    city:str
    firstname:str = "Jan"
    lastname:str = "Kot"
    age:int = 30
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    
    # def __init__(self,firstname,lastname,age):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.age = age

    def __repr__(self):
        return f'Pracownik {self.firstname} {self.lastname}, stanowisko: {self.job}'

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname


os1 = Person("Kraków","małopolskie",True)
print(os1)
print(os1.age)
print(os1.full_name)

print("_"*50)
os2 = Person("Lublin","lubelskie",True,"Anna","Kowal",40,"prezes zarządu")
print(os2)
print(os2.full_name)

print("_"*50)

print(astuple(os1))
print(astuple(os2))

print("_"*50)

print(asdict(os1))
print(asdict(os2))
