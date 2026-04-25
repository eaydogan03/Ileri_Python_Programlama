class CartItem:

    #class attributes
    discount_rate=0.2
    item_count=0

    #constructor
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

#print(CartItem.item_count)

item1=CartItem("Telefon",80000,2)
item2=CartItem("Bilgisayar",90000,1)
item3=CartItem("Tablet",20000,2)

# print(CartItem.item_count)
# print(item3.item_count)

print(item1.name, item1.price)
item1.appy_discount()
print(item1.price)
item1.price=80000
CartItem.discount_rate=0.1
item1.appy_discount()
print(item1.price)

item2.appy_discount()
print(item2.price)

# print(item1.name, item1.price, item1.quantity)
# item1.appy_discount()
# print(item1.price)
# print(item2.name, item2.price, item2.quantity)
# item2.appy_discount()
# print(item2.price)
# print(item3.name, item3.price, item3.quantity)
# item3.appy_discount()
# print(item3.price)


# print(CartItem.discount_rate)
# print(item1.discount_rate)
