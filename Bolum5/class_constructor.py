class CartItem:
    def __init__( name, price, quantity):
        name=name
        price=price
        quantity=quantity


item1=CartItem("Telefon",80000,2)
item2=CartItem("Bilgisayar",90000,1)
item3=CartItem("Tablet",20000,1)


print(item1.name, item1.price, item1.quantity)
print(item2.name, item2.price, item2.quantity)
print(item3.name, item3.price, item3.quantity)
