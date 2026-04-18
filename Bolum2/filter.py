#sayilar=[-3, 5, 8, -1, -4]
# negatifler=[]

# for i in sayilar:
#     if i<0:
#         negatifler.append(i)

# def negatif(i):
#     return i<0

# negatifler=list(filter(lambda x:x<0, sayilar))

# print(sayilar)
# print(negatifler)

#isimler=["Ayşe", "Ebru", "Ceren", "Ali"]
# A_ileBaslayanlar=[]

# for isim in isimler:
#     if isim.startswith("A"):
#         A_ileBaslayanlar.append(isim)


#A_ileBaslayanlar=list(filter(lambda a: a.startswith("A"), isimler))

#isimler2=["ayşe", "ebru", "ceren", "ali"]
#secilenler=filter(lambda x: x[0]=='a',isimler2)

# a_ile_baslayanlar=list(map(lambda x: x.upper(),filter(lambda x: x[0]=='a',isimler2)))
# print(isimler2)
# print(a_ile_baslayanlar)

users= [
{"username": "ebru_aydogan", "posts": ["Python 101", "İleri Seviye Python", "Data Science"]},
{"username": "btk_akademi", "posts": ["Duyuru", "Yeni Kurs"]},
{"username": "yazilim_ogrencisi", "posts": ["Merhaba Dünya"]},
{"username": "python_coder", "posts": []}
]

# pasifKullanicilar=[]

# for user in users:
#     if len(user["posts"])<2:
#         pasifKullanicilar.append(user)

filtered=filter(lambda user: len(user["posts"])<2, users)

pasifler=list(map(lambda user: user["username"], filtered))

print(pasifler)
