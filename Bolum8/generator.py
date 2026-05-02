def count(max):
    sayilar=[]
    sayi = 0
    while sayi <= max:
        sayilar.append(sayi)
        sayi +=1
    return sayilar

def count_gen(max):
    for i in range(max):
        yield i

# sonuc1=count(15)
# print(sonuc1)

# sonuc2=count_gen(15)
# print(sonuc2)

# print(next(sonuc2))
# print(next(sonuc2))
# print(next(sonuc2))

# for x in sonuc2:
#     print(x)

my_list = [i ** 2 for i in range(5)]
print(my_list)

my_gen = (i ** 2 for i in range(5))
print(my_gen)
print(next(my_gen))