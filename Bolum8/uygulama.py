#1 (1 -∞) aralığındaki her sayının karesini getiren fonksiyon.

# def sayi_uret():
#     sayi=0
#     while True:
#         yield sayi ** 2
#         sayi +=1

# #print(sayi_uret())

# generator=sayi_uret()

# for i in generator:
#     print(i)

#2 Fibonacci serisini hem normal fonksiyon hem de generator fonksiyon ile oluşturun.

def fib_list(max):

    liste = []
    sayi1, sayi2 = 0, 1

    #count = 0
    while len(liste) <= max:
        liste.append(sayi2)
        sayi1, sayi2 = sayi2, sayi1+sayi2
        #count += 1
    
    return liste

#print(fib_list(9000))

def fib_gen(max):

    sayi1, sayi2 = 0, 1
    count = 0

    while count <= max:
        yield sayi2
        sayi1, sayi2 = sayi2, sayi1+sayi2
        count += 1

for i in fib_gen(900):
    print(i)



