def add_or_mult(num1: int, num2: int, operator: str) -> int:
    if operator == "+":
        return num1 + num2
    return num1 * num2


def sub_or_div(num1: int, num2: int, operator: str) -> int:
    if operator == "-":
        return num1 - num2
    return num1 // num2


if __name__ == '__main__':
    print(add_or_mult(3, 2, "+"))
    print(add_or_mult(4, 2, "*"))
    print(sub_or_div(4, 2, "-"))
    print(sub_or_div(6, 2, "/"))
