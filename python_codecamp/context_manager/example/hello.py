import time

with open("hello.txt", "w") as f:
    f.write("Hello to this file")
    print("Hey")

time.sleep(20)
# with문에서 실행, 종료가 한 번에 일어나서 sleep과 상관없이 텍스트 작성이 완료된 파일이 만들어진다.
