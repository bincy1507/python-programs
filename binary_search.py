list = [12,23,34,45,56,67,78,89]
key = 45
l = 0
u = len(list)

for i in range(l,u):
    m = (l+u)//2
    if list[m] == key:
        print(key," found at position ",m)
        break
    else:
        if list[m]>key:
            u=m
        else:
            l=m
    