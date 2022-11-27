# 독립성
### self
>**클래스의 객체는 다른 저장공간을 가지고 독립적으로 동작한다.**  
> Calculator 클래스의 인스턴스, 객체 cal1, cal2은 클래스 메소드 add, sub를 독립적으로 이용하고 있다.  
> self는 클래수 내부의 메소드를 **호출한** 객체를 가리킨다. 덕분에 독립적으로 동작할 수 있는 것이다.
> 인스턴스를 생성하면 .을 이용해 클래스 내부의 메소드를 호출할 수 있으며, 변수 또한 가능하다.

- 참고자료  
[self](http://www.tcpschool.com/python/OOP_class_N_object)
```
>>> cal2 = Calculator(2)
2
>>> cal2.add(11) # 메소드 활용
13
>>> cal2.sub(10)
3
>>> cal2.result # 변수에 접근
3
```

# 클래스 변수
- 클래스로 생성된 객체는 서로 독립적으로 작동하지만, 클래스 변수는 공통으로 사용할 수 있다.
- self는 클래스를 호출한 객체를 가리키므로 클래스 변수를 사용할 때는 self가 아닌 클래스 이름으로 접근하는 것이 좋다.
```py
class Makeword:
    result = ""

    def __init__(self, text):
        Makeword.result += text

    def print_word(self):
        print(Makeword.result)
```
