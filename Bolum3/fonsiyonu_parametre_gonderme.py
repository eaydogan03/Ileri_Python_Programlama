# def topla(a, b):
#     return a+b

# def carpma(a, b):
#     return a*b

# def islem(fnc, x, y):
#     return fnc(x, y)

# print(islem(topla, 30, 40))
# print(islem(carpma, 20, 5))

def kareAl(n):
    return n**2

def kupAl(n):
    return n**3

def liste_isle(fnc, liste):
    sonuc=[]
    for i in liste:
        sonuc.append(fnc(i))
    return sonuc

sayilar=[1,2,3,4,5]

print(liste_isle(kareAl, sayilar))
print(liste_isle(kupAl, sayilar))