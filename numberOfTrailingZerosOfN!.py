def zeros(n):
    sum = 0
    step = 5
    while step < n:
        sum += n // step
        step *= 5
    return sum