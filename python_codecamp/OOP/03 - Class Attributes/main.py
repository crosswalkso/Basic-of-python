class Item:
    # class attribute
    pay_rate = 0.8  # 20% 할인
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert (
            quantity >= 0
        ), f"Quantity {quantity} is not greater than or equal to zero!"

        # assign to self object
        ## instance attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        # instance를 생성할 때마다 집어넣는다.
        # self: instance 자체
        Item.all.append(self)

    def calculate_total_price(self):  # method
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # Item.pay_rate (class attribute)
        # self를 쓰면 instance level로 된다.

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


print(Item.all)  # __repr__
# for instance in Item.all:
#     print(instance.name)
