# def selamlama(fn):
#     def inner(isim):
#         print("Hoşgeldiniz.")
#         fn(isim)
#         print("Görüşmek Üzere.")
#     return inner

# @selamlama
# def gunaydin(isim):
#     print(f"Günaydın, benim adım {isim}.")

# @selamlama
# def iyigünler(isim):
#     print(f"İyi günler, benim adım {isim}.")

# gunaydin("Ebru")
# iyigünler("Ali")

# g=selamlama(gunaydin)
# i=selamlama(iyigünler)

# g()
# i()

def susleyici(func):
    def inner(isim):
        print("---Paketi Açıyoruz---")
        func(isim)
        print("---Paketi Kapatıyoruz---")
    return inner

@susleyici
def selamla(isim):
    print(f"Merhaba {isim}")

selamla("Ebru")
