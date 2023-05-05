class Citizen():
    def __init__(self, f: str = "", l: str = "", a: int = 0) -> None:
        self.first_name = f
        self.last_name = l
        self.age = a

    def set_first_name(self, first_name: str):
        if first_name:
            self.first_name = first_name
        if self.first_name == first_name:
            return True if self.first_name == first_name else False

    def set_last_name(self, last_name: str):
        if last_name:
            self.last_name = last_name
            return True if self.last_name == last_name else False

    def set_age(self, age: int):
        if age is not None:
            self.age = age
            return True if self.age == age else False


class Voter(Citizen):
    """ Voter inherits from Citizen, hence we don't explicitly declare f, l, a"""
    def __init__(self, f: str = "", l: str = "", a: int = 0) -> None:
        super().__init__(f, l, a) # here we basically fire up the super classes constructor to initialize these values.
        self.can_vote = True if self.age >= 18 else False # this is the only state that is created by the Voter constructor.


def test_citizen_and_voter2():
    # Test case 1: Create a Citizen instance with default values
    citizen = Citizen()
    assert citizen.first_name == ""
    assert citizen.last_name == ""
    assert citizen.age == 0

    # Test case 2: Create a Citizen instance with custom values
    citizen = Citizen("John", "Doe", 25)
    assert citizen.first_name == "John"
    assert citizen.last_name == "Doe"
    assert citizen.age == 25

    # Test case 3: Set first name and last name of Citizen
    citizen = Citizen()
    assert citizen.set_first_name("Alice") == True
    assert citizen.set_last_name("Smith") == True
    assert citizen.first_name == "Alice"
    assert citizen.last_name == "Smith"

    # Test case 4: Set age of Citizen
    citizen = Citizen()
    assert citizen.set_age(30) == True
    assert citizen.age == 30

    # Test case 5: Create a Voter instance with default values
    voter = Voter()
    assert voter.first_name == ""
    assert voter.last_name == ""
    assert voter.age == 0
    assert voter.can_vote == False

    # Test case 6: Create a Voter instance with custom values
    voter = Voter("Jane", "Smith", 16)
    assert voter.first_name == "Jane"
    assert voter.last_name == "Smith"
    assert voter.age == 16
    assert voter.can_vote == False

    # Test case 7: Create a Voter instance with age exactly 18
    voter = Voter("Bob", "Doe", 18)
    assert voter.first_name == "Bob"
    assert voter.last_name == "Doe"
    assert voter.age == 18
    assert voter.can_vote == True

    print("All test cases pass.")

# Run the test
test_citizen_and_voter2()

