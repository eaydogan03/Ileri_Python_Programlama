# liste=[1, 2, 3]

# print(len(liste))

# # x=5

# # print(len(x))

# s="Merhaba BTK Akademi"

# print(len(s))


class movie:
    def __init__(self, title, year, director, duration):
        self.title=title
        self.year=year
        self.director=director
        self.duration=duration

    def __repr__(self):
        return f"{self.title}, {self.year} yılında {self.director} tarafından çekilmiştir."
    
    def __len__(self):
        return f"Filmin süresi: {self.duration} dakikadır"
    
    def __del__(self):
        print("Film silindi.")
    


m1=movie("Titanic", 1997, "Nolan", 190)

print(m1.__repr__())
print(m1.__len__())

m1.__del__()
#print(m1.)