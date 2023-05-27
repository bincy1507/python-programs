def highest_even(*args):
    a = []
    for item in args:
        if item % 2 == 0:
            a.append(item)
        else:
            pass
    return max(a)


print(highest_even(2, 3, 4, 5, 6, 7, 10, 12))
