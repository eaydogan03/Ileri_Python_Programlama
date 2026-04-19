#1
# def islem_merkezi(s1, s2):
#     def topla(): 
#         return s1+s2
#     def fark():
#         return s1-s2
#     def bolme():
#         return s1/s2 if s2!=0 else "Hata!"
#     return {
#         "toplam": topla(),
#         "fark": fark(),
#         "bolüm": bolme()
#     }

# print(islem_merkezi(25, 0))

#2
# def logger(seviye):
#     def mesaj_yaz(metin):
#         print (f"[{seviye.upper()}]: {metin}")
#     return mesaj_yaz

# bilgi_log=logger("info")
# hata_log=logger("error")

# bilgi_log("Sistem Çalışıyor.")
# hata_log("Bağlantı Kesildi!")

#3
import math

def kareAl(n):
    return n**2
def kokAl(n):
    return math.sqrt(n)
def hesap_makinesi(liste, islem_fonksiyonu):
    sonuc=[]
    for i in liste:
        sonuc.append(islem_fonksiyonu(i))
    return sonuc

sayilar=[4, 9, 25, 49]
print(sayilar)
print("Kareleri:", hesap_makinesi(sayilar, kareAl))
print("Kökleri:", hesap_makinesi(sayilar, kokAl))


