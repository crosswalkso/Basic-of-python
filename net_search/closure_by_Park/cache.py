def in_cache(func):
    cache = {}

    def wrapper(n):  # closure
        print(cache)  ## !!!!
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]

    return wrapper


# @in_cache
def factorial(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret


factorial = in_cache(factorial)
factorial(3)
factorial(5)
factorial(6)
