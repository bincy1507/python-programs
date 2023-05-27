
def string_split(str):
    print(str)
    list = str.split(" ")
    print(list)
    count = 0
    for i in list:
        print(f'length of {i} = {len(i)}')


str = "My name is bincy biju"
string_split(str)