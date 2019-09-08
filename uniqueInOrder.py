def unique_in_order(iterable):
    a = []
    if len(iterable) > 0:
        a.append(iterable[0])
        for i in range(1,len(iterable)):
            if iterable[i] != iterable[i-1]:
                a.append(iterable[i])
    
    return a


print(unique_in_order('AAAABBBCCDAABBB'))