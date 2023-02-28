# Factory method pattern
# class의 인스턴스를 다양한 방법으로 생성할 수 있다.


class Human:
    species = "Homo Sapiens"

    # 나이를 입력받아 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.use_glasses = False

    # 태어난 년도를 입력받아 생성
    @classmethod
    def from_year(cls, name, year):
        import datetime

        # cls == Human (클래스 자신)
        # return [instance 생성]
        return cls(name, datetime.datetime.now().year - year)


# classmethod는 인스턴스를 생성하지 않고 바로 접근해도 된다.
res = Human.from_year("he", 1990)  # 새로운 Human Class 객체 생성
print(res.age)  # 33
david = Human("David", 32)
new_david = david.from_year("David", 1991)
print(new_david.age)  # 32
