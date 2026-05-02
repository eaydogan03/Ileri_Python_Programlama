# hayvanlar=["kedi", "köpek", "kuş"]

# for h in hayvanlar:
#     if isinstance(h, Kedi):
#         print("miyav")
#     elif isinstance(h, Kopek):
#         print("hav")
#     elif isinstance(h, Kus):
#         print("cik cik")

# class Animal():
#     def speak(self):
#         print("Hayvanlar ses çıkarır.")

# class Dog(Animal):
#     def speak(self):
#         print("Köpek havlıyor.")

# class Cat(Animal):
#     def speak(self):
#         print("Kedi miyavlıyor.")


# d1=Dog()
# d1.speak()

# c1=Cat()
# c1.speak()

import math

class Sekil():
    def __init__(self, kenar1):
        self.kenar1=kenar1

    def alan_hesapla(self):
        return self.kenar1 * self.kenar1
    
class Kare(Sekil):
    pass
    
class Daire(Sekil):
    def alan_hesapla(self):
        return math.pi * (self.kenar1**2)
    
class Dikdortgen(Sekil):
    def __init__(self, kenar1, kenar2):
        super().__init__(kenar1)
        self.kenar2=kenar2

    def alan_hesapla(self):
        return self.kenar1 * self.kenar2

s1=Sekil(5)
print(s1.alan_hesapla())

k1=Kare(6)
print(k1.alan_hesapla())

d1=Daire(4)
print(d1.alan_hesapla())

dk1=Dikdortgen(4,5)
print(dk1.alan_hesapla())
