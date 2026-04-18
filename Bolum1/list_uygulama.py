#1. (1-100) arasındaki sayılardan 12'ye tam bölünebilenleri listeleyin.

# sayilar_12=[sayi for sayi in range(1, 101) if sayi%3==0 and sayi%4==0]
# print(sayilar_12)

#2. "BTK 2026 egitim yili 5. donem" metni içindeki rakamları bulup listeleyin. (isdigit() metodu ile rakam kontrolü yapabilirsiniz.)

# text="BTK 2026 egitim yili 5. donem"
# rakamlar=[char for char in text if char.isdigit()]
# print(rakamlar)

#3. sicakliklar= [10, 2, -3, 5, 0] listesindeki 4 derecenin altındaki değerler yerine "Buzlanma Tehlikesi", diğerlerine "Normal" yazdırın.

# sicakliklar= [10, 2, -3, 5, 0]

# sonuc=["Buzlanma Tehlikesi!" if i<4 else "Normal" for i in sicakliklar]

# print(sicakliklar)
# print(sonuc)

#4. ogrenciler= ["Ali", "Ayşe"] ve notlar = [40, 70] listelerini kullanarak, notu 50'den büyük olanları {isim: not} formatında (sözlük) yazmaya çalışın.

# ogrenciler= ["Ali", "Ayşe"]
# notlar = [40, 70]

# sonuclar=["Geçti" if n>50 else "Kaldı" for n in notlar]
# sozluk={ogrenci:sonuc for ogrenci, sonuc in zip(ogrenciler, sonuclar)}
# print(sozluk)
#5. Aşağıdaki kodu list comp ile yazınız. 

list1=[1, 2, 3]
list2=[10, 20]
carpimlar=[]

for x in list1:
    for y in list2:
        carpimlar.append(x*y)

print(carpimlar)


carpimlar2=[x*y for x in list1 for y in list2]
print(carpimlar2)
