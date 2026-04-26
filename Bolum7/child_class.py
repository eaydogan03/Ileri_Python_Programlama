class Person():
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
        #print("Person sınıfı oluşturuldu.")

    def intro(self):
        print(f"Merhaba benim adım {self.name}.")

class student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number=number
        print("Student sınıfı türetildi")

    def study(self):
        print(f"{self.name} ders çalışıyor.")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch=branch
        print("Teacher sınıfı türetildi")

    def teach(self):
        print(f"{self.name}, {self.branch} dersini anlatıyor.")

    def intro(self):
        print(self.name, self.surname, self.age, self.branch)

# p1=Person("Ebru", "Aydoğan", 37)
# p1.intro()
s1=student("Beril", "Aydoğan", 7, 84)
s1.intro()
s1.study()
t1=teacher("Ayşe", "Koç", 35, "Matematik")
t1.intro()
t1.teach()

