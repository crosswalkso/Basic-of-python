# positional argument, unpacking
# 위치 인수, 언패킹


def infinite_sum(s, *args):
    result = 0
    for arg in args:
        result += arg
    print(s, result)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = "Sum:"
infinite_sum(s, *num)
