# Singleton pattern
# 클래스마다 단 하나의 인스턴스만 허용한다.
# 인스턴스가 있으면 이미 생성된 인스턴스를 반환하고
# 그렇지 않으면 인스턴스를 하나 만든다.


class Singleton:
    __instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = cls(*args, **kwargs)
            return cls.__instance


class MyClass(Singleton):
    pass


a = MyClass.instance()
b = MyClass.instance()
c = MyClass()

print(a is b)  # True
