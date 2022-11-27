# 클래스 이름으로 접근하는 것이 명확하다.
class Makeword:
    result = ""

    def __init__(self, text):
        Makeword.result += text

    def print_word(self):
        print(Makeword.result)


# 클래수 변수가 list일때는 self를 써도 공유 가능하지만 문자열("")이라면 공유되지 않는다
# 결론은 클래스 이름으로 접근하는 것이 명확하다.
class Makeword2:
    result = []

    def __init__(self, text):
        self.result += text

    def print_word(self):
        print(self.result)


# 틀림
class Makeword_error:
    result = ""

    def __init__(self, text):
        self.result += text

    def print_word(self):
        print(self.result)


if __name__ == "__main__":
    print("=====클래스 이름으로 접근=====")
    p = Makeword("p")
    y = Makeword("y")
    t = Makeword("t")
    h = Makeword("h")
    o = Makeword("o")
    n = Makeword("n")

    p.print_word()
    n.print_word()

    print("=====리스트 self로 접근=====")
    x = Makeword2("x")
    y = Makeword2("y")

    x.print_word()
    y.print_word()

    print("=====문자열 self로 접근=====")

    a = Makeword_error("a")
    b = Makeword_error("b")
    c = Makeword_error("c")
    d = Makeword_error("d")
    e = Makeword_error("e")

    a.print_word()
    c.print_word()
    d.print_word()
