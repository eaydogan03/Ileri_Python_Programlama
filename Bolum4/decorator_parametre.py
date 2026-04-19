# def double(fn):
#     def inner(*args, **kwargs):
#         fn(*args, **kwargs)
#         return fn(*args, **kwargs)
#     return inner

# @double
# def merhaba():
#     print("Merhaba")

# @double
# def selam(isim):
#     print(f"Selam {isim}")

# @double
# def iyigünler():
#     return "İyi günler"
    

# merhaba()
# selam("Ali")

# print(iyigünler())

def rapor_dec(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} fonksiyonu çağırıldı.")
        sonuc=func(*args, **kwargs)
        print(sonuc)
        print("fonksiyon başarıyla çalıştı.")
        #return sonuc
    return wrapper

@rapor_dec
def topla(a, b):
    return a+b

#print(topla(7,8))
topla(7,8)