# x=5

# print(type(x))
# print(type(int))
# print(type(type))

class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
        print("Person sınıfı oluşturuldu.")

    def intro(self):
        print(f"Merhaba benim adım {self.name}.")

print(type(Person))