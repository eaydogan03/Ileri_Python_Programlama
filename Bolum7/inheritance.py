class person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age

class student(person):
    pass


class teacher(person):
    pass


p1=person("Ebru", "Aydoğan", 37)
s1=student("Beril", "Aydoğan", 7)

print(p1.name, p1.surname, p1.age)
print(s1.name, s1.surname, s1.age)