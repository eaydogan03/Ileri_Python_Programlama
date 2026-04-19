# def usAlma(taban):
#     def inner(us):
#         return taban**us
#     return inner

# sonuc=usAlma(5)(3)
# # fn=usAlma(2)
# # sonuc=fn(4)
# print(sonuc)

# def yetki_sorgulama(sayfa):
#     def inner(rol):
#         if rol=="Admin":
#             return f"{rol} rolü {sayfa} sayfasına erişebilir."
#         else:
#             return f"{rol} rolü {sayfa} sayfasına erişemez!"

#     return inner

# yetki=yetki_sorgulama("Ürün Güncelleme")

# print(yetki("Admin"))
# print(yetki("User"))

def islem(islemAdi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpim(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islemAdi=="toplam":
        return toplam
    else:
        return carpim

toplama=islem("toplam")
carpma=islem("carpim")

sonuc_t=toplama(10, 5, 3)
sonuc_c=carpma(10, 20)

sonuc=sonuc_c*sonuc_t

print(sonuc_t)
print(sonuc_c)

print(sonuc)

