# liste=[True, True, True, True]
# sonuc=all(liste)
# print(sonuc)

#notlar=[50, 85, 45, 90, 95]

# sonuc=True

# for n in notlar:
#     if n<50:
#         sonuc=False
#         break

#print([n>=50 for n in notlar])
# sonuc=all([n>=50 for n in notlar])
# print(sonuc)


# liste=[True, True, False, True]
# sonuc=any(liste)
# print(sonuc)


notlar=[50, 85, 45, 90, 100]
# sonuc=False

# for n in notlar:
#     if n==100:
#         sonuc=True
#         break

sonuc=any([n==100 for n in notlar])
print(sonuc)

