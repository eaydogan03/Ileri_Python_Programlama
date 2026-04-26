class person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
        print("Person sınıfı oluşturuldu.")

    def intro(self):
        print(f"Merhaba benim adım {self.name}.")

class student(person):
    pass


class teacher(person):
    pass


p1=Person("Ebru", "Aydoğan", 37)
p1.intro()
s1=student("Beril", "Aydoğan", 7, 84)
s1.intro()
t1=teacher("Ayşe", "Koç", 35, "Matematik")
t1.intro()
