import csv


class Item:
    # class attribute
    pay_rate = 0.8
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

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)  # csv.DictReader object
            items = list(reader)  # class의 dict 정보로 이루어진 list
        for item in items:
            # csv에서 string으로 와서 형변환
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer_method(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        # type 확인 함수
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()  # 정수인지 확인 5.0도 정수로 판단
        elif isinstance(num, int):
            return True
        # 숫자 이외의 값
        else:
            return False

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        )


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert (
            broken_phones >= 0
        ), f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)

# child class를 instantiate하면서 parent class의 all array에도 phone 객체가 들어간다.
# 기본적으로 super.__init__(..)은 parent class의 메소드를 call하기 때문, all 작업은 super로 인해
# parent level에서 이루어진다.
print(Item.all)
print(Phone.all)

item1 = Item("jscPhonev10", 500, 5)
print(Item.all)
