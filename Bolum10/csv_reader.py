import csv
#csv.reader()
# with open('urunler.csv', 'r', encoding='utf-8') as file:
#     reader=csv.reader(file)

#     #print(reader)
#     next(reader)

#     for satir in reader:
#         #print(satir)
#         print(f"Ürün Adı:{satir[1]}, Ürün Fiyatı:{satir[2]}")

#csv.DictReader()

with open('urunler.csv',encoding='utf-8') as file:
    dict_reader=csv.DictReader(file)

    #print(dict_reader)

    for satir in dict_reader:
        #print(satir)
        print(f"Ürün Adı:{satir["Ürün"]}, Ürün Fiyatı:{satir["Fiyat"]}")