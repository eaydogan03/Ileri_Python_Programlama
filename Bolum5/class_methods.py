class CartItem:

    discount_rate=0.2
    item_count=0

    @classmethod
    def display_count(cls):
        return f"{cls.item_count} tane ürün sepete eklendi."
    
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity=data_str.split(",")
        return cls(name, price, quantity)

    def __init__(self, name, price, quantity):
        #instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity
        CartItem.item_count += 1

    #instance methods
    def calculate_total(self):
        return self.price * self.quantity
    
    def appy_discount(self):
        self.price=self.price * (1-CartItem.discount_rate)
        #return self.price

print(CartItem.display_count())

item1=CartItem("Telefon",80000,2)
item2=CartItem("Bilgisayar",90000,1)
item3=CartItem("Tablet",20000,2)

print(CartItem.display_count())

CartItem.create_item("Mouse,2000,3")

print(CartItem.display_count())
