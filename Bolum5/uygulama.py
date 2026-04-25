#1
# class ogrenci:
#     def __init__(self, ad, soyad, ders_notu):
#         self.ad=ad
#         self.soyad=soyad
#         self.ders_notu=ders_notu

#     def durum_sorgula(self):
#         return "Başarılı." if self.ders_notu >= 50 else "Başarısız!"
    

# o1=ogrenci("Ayşe", "Çakır", 95)
# o2=ogrenci("Fatma", "Yılmaz", 45)

# print(o1.__dict__)
# print(o1.durum_sorgula())
# print(o2.__dict__)
# print(o2.durum_sorgula())
        
#2
# class Urun:
#     urun_adet=0

#     def __init__(self, ad):
#         self.ad=ad
#         Urun.urun_adet += 1
    
#     @classmethod
#     def toplam_urun_sayisi(cls):
#         return f"Toplam Ürün: {cls.urun_adet}"

# print(Urun.toplam_urun_sayisi())    
# u1=Urun("Telefon")
# u2=Urun("Bilgisayar")
# u3=Urun("Tablet")
# print(Urun.toplam_urun_sayisi())  

#3
class Robot:
    toplam_robot_sayisi=0

    def __init__(self, ad):
        self.ad=ad
        Robot.toplam_robot_sayisi +=1

    def selamla(self):
        print(f"Merhaba, ben robot {self.ad}")
    
    @classmethod
    def robot_sayisi_sorgula(cls):
        print(f"Şu anda dünyada {cls.toplam_robot_sayisi} tane robot var.")

Robot.robot_sayisi_sorgula()
r1=Robot("I64")
r2=Robot("WALL-i")
r1.robot_sayisi_sorgula()
