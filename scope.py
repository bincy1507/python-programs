def outer():
    x = "local"

    def inner():
        # nonlocal x
        x = "non local"
        print("inner : ", x)
    inner()
    print("outer : ", x)


outer()
# print(x) -> gives error; grabage collection
