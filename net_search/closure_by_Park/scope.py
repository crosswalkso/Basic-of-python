# scope마다 권한, 책임을 주기 위해 세 가지로 나뉘어져 있다
# 다른 영역을 참조할 땐 기본적으로 읽기만 가능하다.
# -> 주소가 변경되지 않는다면(mutable) 수정 가능.
# mutable vs immutable
# 수정가능한(리스트, 딕셔너리) / 수정 불가능한(숫자, 문자열, 튜플)

z = 3  # global


def outer(x):  # nonlocal
    y = 10

    def inner():  # local
        x = 1000
        return x

    return inner()


print(outer(10))


### 읽기
def greetings(x):
    def say_hi():  # nonlocal 영역의 '읽기' 가능
        print(x)

    say_hi()


greetings("안녕하세요?")

### 쓰기: 수정, 할당
# UnboundLocalError: local variable 'x' referenced before assignment
def count(x):
    def increment():
        # nonlocal x  # 참조하고 싶은 영역을 선택
        x += 1
        print(x)

    increment()


count(5)  # error
