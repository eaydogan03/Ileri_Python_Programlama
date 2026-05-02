import re

text="BTK Akademi Python Kursu BTK"

pattern="BTK"

# match=re.search(pattern,text)

# sonuc=match.span()
# sonuc=match.start()
# sonuc=match.end()

match=re.findall(pattern,text)

sonuc=match

sonuc= re.sub(pattern, "Ebru", text)

print(sonuc)