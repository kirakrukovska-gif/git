class Product:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.available:
            self.items.append(product)
            print(f"{product.name} додано до кошика")
        else:
            print(f"{product.name} немає в наявності")

    def remove_product(self, name):
        for p in self.items:
            if p.name == name:
                self.items.remove(p)
                print(f"{name} видалено з кошика")
                break

    def total_price(self):
        total = sum(p.price for p in self.items)
        print(f"загальна вартість - {total}")

    def show_cart(self):
        if len(self.items) == 0:
            print("кошик порожній")
            return
        print("Товари в кошику: ")
        for p in self.items:
            print(f"{p.name} - {p.price}")

p1 = Product("книга", 500, True)
p2 = Product("ручка", 20, False)
p3 = Product("зошит", 50, True)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.show_cart()
cart.total_price()

cart.remove_product("зошит")
cart.show_cart()







    
