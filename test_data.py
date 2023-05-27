def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
print(test_distinct([1,3,5,8,9]))
print(test_distinct([1,1,8,5,2,8]))