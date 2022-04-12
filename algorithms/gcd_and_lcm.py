def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 if num1 else num2


def lcm(num1, num2):
    return (num1 * num2) / gcd(num1, num2)
