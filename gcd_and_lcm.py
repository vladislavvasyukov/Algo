def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 if num1 else num2


def lcm(num1, num2):
    return (num1 * num2) / gcd(num1, num2)


if __name__ == '__main__':
    print(gcd(12, 30))
    print(gcd(120, 15))
    print(gcd(220, 300))

    print(lcm(12, 30))
    print(lcm(120, 15))
    print(lcm(220, 300))
