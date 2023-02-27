# create a class
class Item:
    def calculate_total(self, x, y):  # method
        return x * y


# create an instance
item1 = Item()

# assign attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# calling methods from instances of a class
print(item1.calculate_total(item1.price, item1.quantity))

# create an instance
item2 = Item()

# assign attributes
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# calling methods from instances of a class
print(item2.calculate_total(item2.price, item2.quantity))
