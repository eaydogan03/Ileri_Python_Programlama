import csv

#csv.writer()
# with open('urunler3.csv', 'w', encoding='utf-8', newline='') as file:
#     writer=csv.writer(file)

#     writer.writerow(['Ürün','Fiyat'])
#     writer.writerow(['Laptop', '25000'])

#     urunler=[['Mouse','4500'], ['Klavye','7800'], ['Monitor','10000']]
#     writer.writerows(urunler)

#csv.DictWriter()
fieldNames=["Ürün", "Fiyat"]
urunler=[
    {'Ürün':'Laptop','Fiyat':'25000'},
    {'Ürün':'Mouse','Fiyat':'4500'},
    {'Ürün':'Klavye','Fiyat':'7800'}
]

with open('urunler3.csv', 'w', encoding='utf-8', newline='') as file:
    writer=csv.DictWriter(file, fieldnames=fieldNames)

    writer.writeheader()
    writer.writerows(urunler)

    writer.writerow({'Ürün':'Monitor','Fiyat':'20000'})

print("Dosya Oluşturuldu")
