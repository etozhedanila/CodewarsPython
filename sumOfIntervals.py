def sum_of_intervals(intervals):
    result = []
    for elem in intervals:
        for i in range(elem[0] + 1, elem[1] + 1):
            result.append(i)
    result = set(result)
    return len(result)