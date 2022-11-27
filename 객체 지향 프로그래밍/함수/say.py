# 초기값
def say(name, old, man=True):
    if man:
        print("man")
    else:
        print("woman")
    print("이름:", name)
    print("나이:", old)


say("python", "11", man=False)  # 초기값 설정은 마지막에
