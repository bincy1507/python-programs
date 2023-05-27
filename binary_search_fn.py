def bin_search(list, key):
    l = 0
    u = len(list)

    for i in range(l, u):
        m = (l+u)//2
        if list[m] == key:
            print(key, " found at position ", m)
            return True
        else:
            if list[m] > key:
                u = m
            else:
                l = m


list = [3, 8, 13, 23, 45, 81]
key = 23
bin_search(list, key)
