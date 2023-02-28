class Human:
    species = "Homo Sapiens"

    def __init__(self, name, age):
        pass

    @staticmethod
    def humanify_number(n):
        return f"{n:,}"


print(Human.humanify_number(1000))
print(Human.humanify_number(10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1))
