# for i in liste:
#     if(koşul):
#         espression

#[expression for item in liste if koşul]

#sayilar=[2, 5, 8, 13, 24, 41]
# ciftler=[]

# for i in sayilar:
#     if(i%2 == 0):
#         ciftler.append(i)

# ciftler=[i for i in sayilar if (i%2==0)]
# print(sayilar)
# print(ciftler)

# sehirler=["Ankara", "Afyon", "Eskişehir", "Van"]

# a_olanlar=[sehir for sehir in sehirler if "a" in sehir.lower()]

# print(sehirler)
# print(a_olanlar)

notlar=[40, 45, 55, 90, 95]
# sonuc=[]

# for n in notlar:
#     if(n>=50):
#         sonuc.append("Geçti")
#     else:
#         sonuc.append("Kaldı")

sonuc=[n if n>=50  else "Kaldı" for n in notlar]

print(notlar)
print(sonuc)