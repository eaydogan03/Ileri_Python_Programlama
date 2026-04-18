# liste=[25, 10, 5, 80, 33]
# print(liste)
# print(sorted(liste, reverse=True))

# stok={"Elma":50, "Cilek":100, "Muz":20}
# sirali=sorted(stok)

# print(sirali)

#dict={key:value}

# urunler=[
#     {"ad":"Laptop", "fiyat": 1000},
#     {"ad":"Telefon", "fiyat": 900},
#     {"ad":"Tablet", "fiyat": 700}
# ]

# sirali_urunler=sorted(urunler,key=lambda x: x["fiyat"])
# print(sirali_urunler)

isimler=["Ebru", "Ayşe", "Abdullah", "Zeynep"]
sirali_isimler=sorted(isimler, key=lambda x: len(x))

print(sirali_isimler)