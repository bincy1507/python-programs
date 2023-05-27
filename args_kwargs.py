# *args and **kwargs

def fn_1(*args,**kwargs):
    print(args)
    print(sum(args))
    print(kwargs.keys())
    total = 0
    for i in kwargs.values():
        total += i
    return total + sum(args)
print(fn_1(1,2,3,num1=3,num2=5))

