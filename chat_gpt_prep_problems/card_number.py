def number(s):
    num = f"{s[0:3]} **** **** {s[12:]}"
    return num

print(number("1234567890123467"))