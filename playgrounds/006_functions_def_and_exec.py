
def addition_with_default_args(a: int, b: int = 3) -> int:
    print("a:", a, "b:", b)
    return a + b

# calling with arguments based on positions.
answ = addition_with_default_args(1, 2)  # 1 + 2 = 3
print("func(1,2):", answ)  # 3

# executing this function with the default argument 'b'
answ = addition_with_default_args(2)  # 2 + 3 = 5
print("func(2):", answ)  # 3

# executing this function by moving args around
answ = addition_with_default_args(b=4,a=9)
print("func(b=4,a=9):", answ)  # 3

