class FileManager:
    def __init__(self,filename,mode,encode):
        self.filename = filename
        self.mode = mode
        self.encode = encode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('testowy.txt','w','utf-8') as f:
    f.write("to jest ważna informacja do zapisu....")

print(f.closed)

h = open("testowy.txt","w",encoding="utf-8")
h.write("dodatek...")

h.close()
print("____________")
print(h.closed)
print(f.closed)

print("____________")


with open("drugi.csv","w",encoding="utf-8") as g:
    g.write("id,nazwa,ilość,cena")

print(g.closed)

with FileManager("drugi.csv","r","utf-8") as f:
    print(f.read())

