# def selam(isim):
#     print(f"Merhaba {isim}")

# merhaba=selam


# selam("Ebru")


# del selam

# #print(selam)
# print(merhaba)
# merhaba("Ali")

# def outer(number):
#     print("Merhaba")   
#     def inner():
#          print(f"Girdiğiniz sayı: {number}")
#     inner()

# outer(15)
# def factorial(number):
#     def inner():
#         sonuc=1
#         for i in range(1, number+1):
#             sonuc*=i 
#         return sonuc
#     return inner()

# print(factorial(4))


def factorial_rec(number):
    if not isinstance(number, int):
        raise TypeError("Number must be integer!")
    
    if not number>=0:
        raise ValueError("Number must be zero or positive!")

    def inner(number):
        if number<=1:
            return 1
        return number*inner(number-1)
    
    return inner(number)

#sonuc=factorial_rec(5)
try: 
    sonuc=factorial_rec(5)
    print(sonuc)
except Exception as ex:
    print(ex)







    