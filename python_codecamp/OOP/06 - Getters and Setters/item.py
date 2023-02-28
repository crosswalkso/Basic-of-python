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
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    # property decorator = read-only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # 수정할 때만 먹히는 제약
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

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
