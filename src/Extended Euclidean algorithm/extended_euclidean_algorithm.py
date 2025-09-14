def extended_gcd(a, b):
    x, x_prev, y, y_prev = 0, 1, 1, 0

    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x, x_prev, y, y_prev = x_prev - (quotient * x), x, y_prev - (quotient * y), y

    return abs(a), x_prev, y_prev


if __name__ == "__main__":
    first_number = int(input("Input first number: "))
    second_number = int(input("Input second number: "))

    gcd, x, y = extended_gcd(first_number, second_number)
    print(f"gcd = {gcd}, x = {x}, y = {y}")
    print(f"{first_number} * {x} + {second_number} * {y} = {gcd}")
