
from xml.dom.minidom import  parse

dom = parse("dane.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')
url = dom.getElementsByTagName('url')
opis = dom.getElementsByTagName('opis')
for op in opis:
    opisattr = op.getAttribute("desc")
    dw = op.getAttribute("datawpisu")
    print(f"atrybuty opis -> desc = {opisattr}, datawpisu = {dw}")

print("_" * 30)

print("   ".join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE))
print("_"*30)
print("   ".join(t.nodeValue for t in opis[0].childNodes if t.nodeType == t.TEXT_NODE))
print("_"*30)
print("   ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType == t.TEXT_NODE))
print("_"*30)
print("   ".join(t.nodeValue for t in kod[1].childNodes if t.nodeType == t.TEXT_NODE))
print("_"*30)
print("   ".join(t.nodeValue for t in url[0].childNodes if t.nodeType == t.TEXT_NODE))
print("_"*30)
print("   ".join(t.nodeValue for t in url[0].childNodes if t.nodeType == t.TEXT_NODE))
print("_"*30)
