class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert (
            quantity >= 0
        ), f"Quantity {quantity} is not greater than or equal to zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):  # method
        return self.price * self.quantity


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
# item2.has_numpad = False  # instantiate 후에도 attribute 가능

print(item1.calculate_total_price())
print(item2.calculate_total_price())
