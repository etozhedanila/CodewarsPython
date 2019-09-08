def last_digit(n1, n2):
    p = n2 % 100 % 4 if n2 % 100 % 4 != 0 else 4
    return ((n1 % 10) ** p) % 10 if n2 != 0 else 1


print(last_digit(12, 120))