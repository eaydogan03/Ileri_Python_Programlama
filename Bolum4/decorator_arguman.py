# def selamlama_dec(count):   
#     def selamlama(fn):
#         def inner(isim):
#             for i in range(count):
#                 fn(isim)
#         return inner
#     return selamlama

# @selamlama_dec(count=5)
# def merhaba(isim):
#     print(f"Merhaba {isim}")

# @selamlama_dec(3)
# def selam(isim):
#     print(f"Selam {isim}")

# merhaba("Ebru")
# selam("Ali")

def dec_yetki_kontrol(rol):
    def yetki_kontrol(func):
        def inner(*args, **kwargs):
            kullanici_rolu="Admin"
            if kullanici_rolu==rol:
                return func(*args, **kwargs)
            else:
                return(f"Hata: Bunu çalıştırmak için {rol} olmalısınız!")
        return inner
    return yetki_kontrol

@dec_yetki_kontrol("Admin")
def admin_sayfa():
    return "Admin paneline Hoşgeldiniz."

print(admin_sayfa())
    