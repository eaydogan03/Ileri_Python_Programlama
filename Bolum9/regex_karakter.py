import re

text="AABC 123 983 1A3 1_2 354 2 78 23458 Aabc"

# pattern=r"\d\d\d"
#pattern=r"\d{3}"
#pattern=r"\d+"
# pattern=r"\d{3,5}"
pattern=r"[a-zA-Z]{3}"

# match=re.search(pattern, text)
match=re.findall(pattern, text)

sonuc=match

print(sonuc)

# match=re.finditer(pattern, text)

# for i in match:
#     print(i.group())
