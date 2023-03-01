import time

f = open("hello2.txt", "w")
f.write("Hello to this file")

print(f.closed)  # False

time.sleep(20)
# txt파일은 만들어지나, sleep이 끝난 후 문자가 기록된다.
