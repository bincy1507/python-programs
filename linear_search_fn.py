def linear_search(list, key):
    for i in range(len(list)):
        if list[i] == key:
            print(key, " found at position ", i)
            break
    else:
        print("Not found")


list = [4, 7, 3, 9, 5, 8, 6, 1, 2]
key = 11

linear_search(list, key)
