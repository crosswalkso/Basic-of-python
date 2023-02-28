class Cat:
    species = "Felis Catus"

    @classmethod
    def get_species(cls):
        print(f"Scientific name for cat is {cls.species}!")


# Cat.get_species = classmethod(Cat.get_species) -> 데코레이터로 역할 대체

Cat.get_species()
