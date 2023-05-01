class Citizen():
    def __init__(self, f: str = "", l: str = "", a: int = 0) -> None:
        self.first_name = f
        self.last_name = l
        self.age = a

    def set_first_name(self, first_name: str):
        if first_name:
            self.first_name = first_name
            return True
        return False

    def set_last_name(self, last_name: str):
        if last_name:
            self.first_name = last_name
            return True
        return False

    def set_age(self, age: int):
        self.age = age
        return True


class Voter(Citizen):
    def __init__(self, f: str = "", l: str = "", a: int = 0) -> None:
        super().__init__(f, l, a)
        self.can_vote = True if self.age >= 18 else False


citizen_1 = Voter("George", "Le Mieux", 63)
citizen_2 = Voter("Genny", "La Grande", 8)
print("Citizen:name:", citizen_1.first_name, citizen_1.last_name,
      "Can Vote:", "Yes" if citizen_1.can_vote else "No")
print("Citizen:name:", citizen_2.first_name, citizen_2.last_name,
      "Can Vote:" "Yes" if citizen_2.can_vote else "No")
